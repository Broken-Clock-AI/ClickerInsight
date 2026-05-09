import { create } from 'zustand';
// @ts-ignore
import Decimal from 'break_infinity.js';
import { defineInitialState, type GameState } from '../types/GameState';
import GameData from '../data/GameDesignDocument_v5.json';

interface GameActions {
    click: () => void;
    buyGenerator: (generatorId: string) => void;
    tick: (deltaTime: number) => void;
    prestige: (layerId: string) => void;
    hardReset: () => void;
    getEfficiencyScore: (generatorId: string) => Decimal;
    checkParadigmShifts: () => void;
}

// DEMAINE-2018-01: Item Costing (Exponential Growth)
// Formula: Cn = C1 * alpha^(n)
const calculateCost = (baseCost: number, scaling: number, owned: Decimal) => {
    return new Decimal(baseCost).times(new Decimal(scaling).pow(owned));
};

export const useGameStore = create<GameState & GameActions>((set, get) => ({
    ...defineInitialState(),

    click: () => {
        const clickValue = GameData.coreLoop.manualClickValue.baseValue;
        set((state) => ({
            currency: state.currency.plus(clickValue),
            lifetimeCurrency: state.lifetimeCurrency.plus(clickValue),
        }));
    },

    buyGenerator: (generatorId: string) => {
        const state = get();
        const generatorConfig = GameData.generators.find(g => g.id === generatorId);
        if (!generatorConfig) return;

        const currentOwned = state.generators[generatorId]?.owned || new Decimal(0);
        const cost = calculateCost(generatorConfig.baseCost, generatorConfig.costScaling, currentOwned);

        if (state.currency.gte(cost)) {
            set((state) => ({
                currency: state.currency.minus(cost),
                generators: {
                    ...state.generators,
                    [generatorId]: {
                        ...state.generators[generatorId],
                        id: generatorId,
                        owned: currentOwned.plus(1),
                        appliedMultipliers: state.generators[generatorId]?.appliedMultipliers || new Decimal(1)
                    }
                }
            }));
            state.checkParadigmShifts();
        }
    },

    tick: (deltaTime: number) => {
        const state = get();
        const nextGenerators = { ...state.generators };
        let nextCurrency = state.currency;
        let nextLifetime = state.lifetimeCurrency;

        // Process generator outputs
        GameData.generators.forEach(gen => {
            const owned = state.generators[gen.id]?.owned || new Decimal(0);
            if (owned.gt(0)) {
                const multiplier = state.generators[gen.id]?.appliedMultipliers || new Decimal(1);
                const amount = owned.times(gen.output.baseRate).times(multiplier).times(deltaTime);

                if (gen.output.type === 'currency') {
                    nextCurrency = nextCurrency.plus(amount);
                    nextLifetime = nextLifetime.plus(amount);
                } else if (gen.output.type === 'generator') {
                    const targetId = gen.output.targetId;
                    const targetOwned = nextGenerators[targetId]?.owned || new Decimal(0);
                    nextGenerators[targetId] = {
                        ...nextGenerators[targetId],
                        id: targetId,
                        owned: targetOwned.plus(amount),
                        appliedMultipliers: nextGenerators[targetId]?.appliedMultipliers || new Decimal(1)
                    };
                }
            }
        });

        set({
            currency: nextCurrency,
            lifetimeCurrency: nextLifetime,
            generators: nextGenerators,
            lastTick: Date.now()
        });
    },

    getEfficiencyScore: (generatorId: string) => {
        const state = get();
        const config = GameData.generators.find(g => g.id === generatorId);
        if (!config) return new Decimal(Infinity);

        const cost = calculateCost(config.baseCost, config.costScaling, state.generators[generatorId]?.owned || new Decimal(0));
        
        // Calculate Global Generation Rate (G)
        let G = new Decimal(0);
        GameData.generators.forEach(gen => {
            if (gen.output.type === 'currency') {
                const owned = state.generators[gen.id]?.owned || new Decimal(0);
                const mult = state.generators[gen.id]?.appliedMultipliers || new Decimal(1);
                G = G.plus(owned.times(gen.output.baseRate).times(mult));
            }
        });

        if (G.eq(0)) G = new Decimal(0.01); // Avoid div by zero

        // Effective Rate Increase (xi)
        let xi = new Decimal(config.output.baseRate);
        if (config.output.type === 'generator') {
            // Recursive estimation: what's the rate of the target?
            const target = GameData.generators.find(t => t.id === config.output.targetId);
            if (target && target.output.type === 'currency') {
                xi = xi.times(target.output.baseRate);
            }
        }

        // DEMAINE-2018-02: Ei = (yi / xi) + (yi / G)
        return cost.div(xi).plus(cost.div(G));
    },

    checkParadigmShifts: () => {
        const state = get();
        GameData.paradigmShifts?.forEach(shift => {
            if (state.paradigmShiftsAchieved.includes(shift.id)) return;

            const conditionsMet = shift.unlockConditions.every(cond => {
                if (cond.type === 'currency_owned') {
                    return state.currency.gte(cond.value);
                }
                if (cond.type === 'generator_owned') {
                    return (state.generators[cond.targetId]?.owned || new Decimal(0)).gte(cond.value);
                }
                return false;
            });

            if (conditionsMet) {
                set(s => ({
                    paradigmShiftsAchieved: [...s.paradigmShiftsAchieved, shift.id],
                    unlockedMechanics: [...new Set([...s.unlockedMechanics, ...shift.newMechanicsUnlocked])]
                }));
            }
        });
    },

    prestige: (layerId: string) => {
        const state = get();
        const layer = GameData.prestige.layers.find(l => l.id === layerId);
        if (!layer) return;

        // Formula: floor(5 * cbrt(currency.insight / 1e12))
        // We'll use a safer decimal version
        const insight = state.currency;
        const wisdomGain = new Decimal(5).times(insight.div(1e12).pow(1/3)).floor();

        if (wisdomGain.gt(0)) {
            const currentWisdom = state.prestigeCurrencies[layer.currencyName.toLowerCase()] || new Decimal(0);
            set({
                ...defineInitialState(),
                prestigeCurrencies: {
                    ...state.prestigeCurrencies,
                    [layer.currencyName.toLowerCase()]: currentWisdom.plus(wisdomGain)
                },
                unlockedMechanics: state.unlockedMechanics // Preserve unlocks? Usually prestige resets some but not all.
            });
        }
    },

    hardReset: () => {
        set(defineInitialState());
    }

}));

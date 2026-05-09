import { create } from 'zustand';
// @ts-ignore
import Decimal from 'break_infinity.js';
import { defineInitialState, type GameState } from '../types/GameState';
import GameData from '../data/GameDesignDocument.json';

interface GameActions {
    click: () => void;
    buyGenerator: (generatorId: string) => void;
    tick: (deltaTime: number) => void;
    prestige: () => void;
    hardReset: () => void;
}

// Helper to calculate cost: Base * (Multiplier ^ Owned)
const calculateCost = (baseCost: number, multiplier: number, owned: Decimal) => {
    return new Decimal(baseCost).times(new Decimal(multiplier).pow(owned));
};

export const useGameStore = create<GameState & GameActions>((set, get) => ({
    ...defineInitialState(),

    click: () => {
        set((state) => ({
            currency: state.currency.plus(GameData.baseClickPower),
            lifetimeCurrency: state.lifetimeCurrency.plus(GameData.baseClickPower),
        }));
    },

    buyGenerator: (generatorId: string) => {
        const state = get();
        const generatorConfig = GameData.generators.find(g => g.id === generatorId);
        if (!generatorConfig) return;

        const currentOwned = state.generators[generatorId]?.owned || new Decimal(0);
        const cost = calculateCost(generatorConfig.baseCost, generatorConfig.costMultiplier, currentOwned);

        if (state.currency.gte(cost)) {
            set((state) => ({
                currency: state.currency.minus(cost),
                generators: {
                    ...state.generators,
                    [generatorId]: {
                        id: generatorId,
                        owned: (state.generators[generatorId]?.owned || new Decimal(0)).plus(1)
                    }
                }
            }));
        }
    },

    tick: (deltaTime: number) => {
        // DeltaTime is in seconds
        const state = get();
        let productionPerSecond = new Decimal(0);

        GameData.generators.forEach(gen => {
            const owned = state.generators[gen.id]?.owned || new Decimal(0);
            if (owned.gt(0)) {
                productionPerSecond = productionPerSecond.plus(owned.times(gen.baseProduction));
            }
        });

        if (productionPerSecond.gt(0)) {
            const production = productionPerSecond.times(deltaTime);
            set((state) => ({
                currency: state.currency.plus(production),
                lifetimeCurrency: state.lifetimeCurrency.plus(production),
                lastTick: Date.now()
            }));
        }
    },

    prestige: () => {
        // TODO: Implement prestige logic defined in GameDesignDocument
        console.log("Prestige not yet implemented");
    },

    hardReset: () => {
        set(defineInitialState());
    }

}));

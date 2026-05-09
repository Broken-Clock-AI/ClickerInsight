// @ts-ignore
import Decimal from 'break_infinity.js';
import { useGameStore } from '../hooks/useGameStore';
import GameData from '../data/GameDesignDocument_v5.json';

// Helper to format cost
const formatNumber = (num: Decimal): string => {
    if (num.lt(1000)) return num.toFixed(0);
    return num.toExponential(2).replace('+', '');
};

export const GeneratorList = () => {
    const { generators, currency, buyGenerator, getEfficiencyScore } = useGameStore();

    // DEMAINE-2018-01: Cost calculation
    const getCost = (id: string) => {
        const config = GameData.generators.find(g => g.id === id);
        if (!config) return new Decimal(0);
        const owned = generators[id]?.owned || new Decimal(0);
        return new Decimal(config.baseCost).times(new Decimal(config.costScaling).pow(owned));
    };

    // Find the next best investment based on Efficiency Score (Demaine-2018)
    const sortedGens = [...GameData.generators].sort((a, b) => {
        const scoreA = getEfficiencyScore(a.id);
        const scoreB = getEfficiencyScore(b.id);
        return scoreA.sub(scoreB).toNumber();
    });

    const bestInvestment = sortedGens[0];

    return (
        <div className="flex flex-col gap-3">
            {/* Efficiency Recommendation */}
            {bestInvestment && (
                <div className="mb-4 p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-lg flex justify-between items-center">
                    <div className="flex flex-col">
                        <span className="text-emerald-300 text-xs font-bold uppercase tracking-wide">Optimal Decision (RKA-01)</span>
                        <span className="text-emerald-100 font-bold">{bestInvestment.name}</span>
                    </div>
                    <div className="text-right">
                        <span className="text-emerald-400 text-xs block">Efficiency Score</span>
                        <span className="text-white font-mono text-sm">{formatNumber(getEfficiencyScore(bestInvestment.id))}</span>
                    </div>
                </div>
            )}

            <h2 className="text-sm font-bold mb-2 text-slate-400 uppercase tracking-widest pl-1">
                Machinic Nodes
            </h2>
            {GameData.generators.map((gen) => {
                const owned = generators[gen.id]?.owned || new Decimal(0);
                const cost = getCost(gen.id);
                const canAfford = currency.gte(cost);
                const efficiency = getEfficiencyScore(gen.id);

                // Progress: 0 to 100
                const progress = cost.eq(0) ? 100 : Math.min(100, currency.div(cost).times(100).toNumber());

                return (
                    <button
                        key={gen.id}
                        onClick={() => buyGenerator(gen.id)}
                        disabled={!canAfford}
                        className={`
                            relative overflow-hidden w-full text-left
                            flex justify-between items-center p-4 rounded-xl border border-slate-700
                            transition-all duration-200 group
                            bg-slate-800
                            ${canAfford
                                ? 'hover:bg-slate-700 hover:border-emerald-500/50 cursor-pointer shadow-lg hover:-translate-y-0.5'
                                : 'cursor-not-allowed'}
                        `}
                    >
                        {/* Progress Bar Background */}
                        <div
                            className="absolute left-0 top-0 bottom-0 bg-emerald-500/10 transition-all duration-300 ease-out z-0"
                            style={{ width: `${progress}%` }}
                        />

                        {/* Content */}
                        <div className="relative z-10 flex flex-col">
                            <span className={`font-bold text-lg ${canAfford ? 'text-white' : 'text-slate-400'}`}>
                                {gen.name}
                            </span>
                            <div className="flex gap-2 items-center">
                                <span className="text-[10px] text-slate-500 font-mono uppercase tracking-tighter bg-slate-900 px-1 rounded">
                                    {gen.nodeType}
                                </span>
                                <span className="text-xs text-slate-400 font-mono">
                                    Owned: <span className="text-slate-200">{owned.toFixed(0)}</span>
                                </span>
                            </div>
                        </div>

                        <div className="relative z-10 text-right flex flex-col items-end">
                            <span className={`font-mono font-medium text-sm ${canAfford ? 'text-emerald-400' : 'text-slate-500'}`}>
                                {formatNumber(cost)} {GameData.coreLoop.primaryCurrency.name}
                            </span>
                            <div className="flex flex-col items-end gap-0.5 text-[10px] text-slate-500 mt-1 font-mono">
                                <span>Yield: {gen.output.baseRate}/s</span>
                                <span className="text-slate-600">E-Score: {formatNumber(efficiency)}</span>
                            </div>
                        </div>
                    </button>
                );
            })}
        </div>
    );
};

// @ts-ignore
import Decimal from 'break_infinity.js';
import { useGameStore } from '../hooks/useGameStore';
import GameData from '../data/GameDesignDocument.json';

// Helper to format cost
const formatCost = (num: Decimal): string => {
    if (num.lt(1000)) return num.toFixed(0);
    return num.toExponential(2);
};

export const GeneratorList = () => {
    const { generators, currency, buyGenerator } = useGameStore();

    // Find the next affordable goal for the "Short-term Goal" indicator
    const nextGoal = GameData.generators.find(gen => {
        const owned = generators[gen.id]?.owned || new Decimal(0);
        const cost = new Decimal(gen.baseCost).times(new Decimal(gen.costMultiplier).pow(owned));
        return currency.lt(cost);
    });

    return (
        <div className="flex flex-col gap-3">
            {/* Next Goal Indicator */}
            {nextGoal && (
                <div className="mb-4 p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-lg flex justify-between items-center animate-pulse">
                    <span className="text-indigo-300 text-sm font-bold uppercase tracking-wide">Next Goal</span>
                    <div className="text-right">
                        <span className="text-indigo-100 font-bold">{nextGoal.name}</span>
                        <span className="text-indigo-400 text-xs ml-2">
                            at {formatCost(new Decimal(nextGoal.baseCost).times(new Decimal(nextGoal.costMultiplier).pow(generators[nextGoal.id]?.owned || 0)))}
                        </span>
                    </div>
                </div>
            )}

            <h2 className="text-sm font-bold mb-2 text-slate-400 uppercase tracking-widest pl-1">
                Automation Units
            </h2>
            {GameData.generators.map((gen) => {
                const owned = generators[gen.id]?.owned || new Decimal(0);
                const cost = new Decimal(gen.baseCost).times(new Decimal(gen.costMultiplier).pow(owned));
                const canAfford = currency.gte(cost);

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
                            className="absolute left-0 top-0 bottom-0 bg-emerald-500/20 transition-all duration-300 ease-out z-0"
                            style={{ width: `${progress}%` }}
                        />

                        {/* Content */}
                        <div className="relative z-10 flex flex-col">
                            <span className={`font-bold text-lg ${canAfford ? 'text-white' : 'text-slate-400'}`}>
                                {gen.name}
                            </span>
                            <span className="text-xs text-slate-400 font-mono mt-0.5">
                                Owned: <span className="text-slate-200">{owned.toString()}</span>
                            </span>
                        </div>

                        <div className="relative z-10 text-right flex flex-col items-end">
                            <span className={`font-mono font-medium text-sm ${canAfford ? 'text-emerald-400' : 'text-slate-500'}`}>
                                {formatCost(cost)} {GameData.currencyName}
                            </span>
                            <div className="flex items-center gap-1 text-xs text-slate-500 mt-1">
                                <span>+{gen.baseProduction}/s</span>
                            </div>
                        </div>

                        {/* Lock Overlay Icon */}
                        {!canAfford && (
                            <div className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-600/20 text-4xl pointer-events-none">
                                🔒
                            </div>
                        )}
                    </button>
                );
            })}
        </div>
    );
};

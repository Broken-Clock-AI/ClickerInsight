// @ts-ignore
import Decimal from 'break_infinity.js';

interface CurrencyDisplayProps {
    amount: Decimal;
    label: string;
}

const formatNumber = (num: Decimal): string => {
    if (num.lt(1000)) return num.toFixed(0);
    // RKA Principle 1: Machinic Thinking - prioritize scientific notation for large scales
    return num.toExponential(2).replace('+', '');
};

export const CurrencyDisplay = ({ amount, label }: CurrencyDisplayProps) => {
    return (
        <div className="text-center p-4">
            <div className="text-4xl font-bold font-mono text-emerald-400 drop-shadow-lg">
                {formatNumber(amount)}
            </div>
            <div className="text-sm uppercase tracking-widest text-emerald-200/50 mt-1">
                {label}
            </div>
        </div>
    );
};

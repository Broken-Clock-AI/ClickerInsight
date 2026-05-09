// @ts-ignore
import Decimal from 'break_infinity.js';

interface CurrencyDisplayProps {
    amount: Decimal;
    label: string;
}

const formatNumber = (num: Decimal): string => {
    if (num.lt(1000)) return num.toFixed(0);
    if (num.lt(1e6)) return (num.div(1000)).toFixed(2) + 'k';
    if (num.lt(1e9)) return (num.div(1e6)).toFixed(2) + 'm';
    if (num.lt(1e12)) return (num.div(1e9)).toFixed(2) + 'b';
    if (num.lt(1e15)) return (num.div(1e12)).toFixed(2) + 't';
    return num.toExponential(2);
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

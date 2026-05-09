import { useState, useRef } from 'react';
// @ts-ignore
import Decimal from 'break_infinity.js';

interface ClickerButtonProps {
    onClick: () => void;
    amount: Decimal;
}

interface Particle {
    id: number;
    x: number;
    y: number;
    text: string;
}

export const ClickerButton = ({ onClick, amount }: ClickerButtonProps) => {
    const [particles, setParticles] = useState<Particle[]>([]);
    const buttonRef = useRef<HTMLButtonElement>(null);

    const handleClick = (e: React.MouseEvent) => {
        // Trigger game logic
        onClick();

        // Spawn particle
        const rect = buttonRef.current?.getBoundingClientRect();
        if (rect) {
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const newParticle: Particle = {
                id: Date.now() + Math.random(),
                x,
                y,
                text: `+${amount.toString()}`
            };

            setParticles(prev => [...prev, newParticle]);

            // Cleanup particle after animation
            setTimeout(() => {
                setParticles(prev => prev.filter(p => p.id !== newParticle.id));
            }, 800);
        }
    };

    return (
        <div className="relative w-full max-w-md mx-auto aspect-square flex items-center justify-center">
            {/* Outer Glow Ring */}
            <div className="absolute inset-0 bg-emerald-500/20 rounded-full blur-xl animate-pulse-ring"></div>

            <button
                ref={buttonRef}
                onClick={handleClick}
                className="
                    click-feedback-button
                    relative z-10 w-64 h-64 rounded-full 
                    bg-gradient-to-b from-emerald-600 to-emerald-900 
                    border-4 border-emerald-400/50 
                    shadow-[0_0_50px_rgba(16,185,129,0.4)]
                    hover:shadow-[0_0_80px_rgba(16,185,129,0.6)]
                    hover:brightness-110
                    active:shadow-[0_0_20px_rgba(16,185,129,0.4)]
                    transition-all duration-100 ease-out
                    group
                "
            >
                <div className="flex flex-col items-center justify-center h-full text-slate-100 dark:text-white">
                    <span className="text-3xl font-black tracking-wider uppercase drop-shadow-lg">
                        Research
                    </span>
                    <span className="text-sm font-mono text-emerald-200 opacity-80 mt-1">
                        +{amount.lt(1000) ? amount.toString() : amount.toExponential(2).replace('+', '')} Insight
                    </span>
                </div>

                {/* Initial Guide (visible only if first click, but for now just visual) */}
                <div className="absolute -bottom-12 left-1/2 -translate-x-1/2 text-emerald-400 text-sm animate-bounce opacity-50 pointer-events-none">
                    CLICK TO ANALYZE
                </div>
            </button>

            {/* Particle Layer */}
            {particles.map(p => (
                <div
                    key={p.id}
                    className="absolute pointer-events-none animate-float font-bold text-xl text-white drop-shadow-md z-20"
                    style={{
                        left: p.x,
                        top: p.y,
                    }}
                >
                    {p.text}
                </div>
            ))}
        </div>
    );
};

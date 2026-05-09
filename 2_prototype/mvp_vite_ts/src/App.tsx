import { useGameStore } from './hooks/useGameStore';
import { useGameLoop } from './hooks/useGameLoop';
import { CurrencyDisplay } from './components/CurrencyDisplay';
import { GeneratorList } from './components/GeneratorList';
import { ClickerButton } from './components/ClickerButton';
// @ts-ignore
import Decimal from "break_infinity.js";
import GameData from './data/GameDesignDocument_v5.json';
import './App.css';

function App() {
  // Initialize Game Loop
  useGameLoop();

  const { currency, click } = useGameStore();

  return (
    <div className="min-h-screen w-full bg-slate-950 text-slate-200 selection:bg-emerald-500/30 overflow-hidden relative">

      {/* Background Atmospherics */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-slate-950 z-0"></div>
      <div className="absolute inset-0 bg-grid-pattern z-0 opacity-20 pointer-events-none"></div>

      <div className="container mx-auto max-w-6xl p-6 grid gap-12 relative z-10 h-screen grid-rows-[auto_1fr]">

        {/* Header / Resource Display - DOMINANT */}
        <header className="flex flex-col items-center justify-center pt-8 pb-4">
          <CurrencyDisplay amount={currency} label={GameData.coreLoop.primaryCurrency.name} />
          <div className="text-slate-500 text-sm mt-2 tracking-widest uppercase opacity-60">
            Hardened Knowledge Architecture v2.1
          </div>
        </header>

        {/* Main Interface Grid */}
        <main className="grid lg:grid-cols-[1.2fr_1fr] gap-12 items-start h-full pb-8">

          {/* Left Col: The "Work" Area - CENTRAL INTERACTION */}
          <div className="flex flex-col items-center justify-center p-8 h-full">
            <ClickerButton
              onClick={click}
              amount={new Decimal(GameData.coreLoop.manualClickValue.baseValue)}
            />
          </div>

          {/* Right Col: The "Shop" Area - DENSE UI */}
          <div className="bg-slate-900/40 backdrop-blur-sm rounded-3xl border border-slate-800/50 p-6 h-full overflow-hidden flex flex-col">
            <GeneratorList />
          </div>

        </main>

      </div>
    </div>
  );
}

export default App;

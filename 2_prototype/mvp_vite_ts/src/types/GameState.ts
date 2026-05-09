// @ts-ignore
import Decimal from 'break_infinity.js';

export interface GeneratorState {
  id: string;
  owned: Decimal;
  appliedMultipliers: Decimal; // Dynamic multipliers from upgrades/milestones
}

export interface GameState {
  currency: Decimal;
  lifetimeCurrency: Decimal;
  prestigeCurrencies: Record<string, Decimal>; // Maps prestige currency ID to value (e.g., 'wisdom')
  generators: Record<string, GeneratorState>;
  upgradesOwned: string[]; // List of upgrade IDs
  researchNodesOwned: string[]; // List of research node IDs
  unlockedMechanics: string[]; // e.g., ['prestige', 'research_trees']
  paradigmShiftsAchieved: string[];
  lastTick: number;
}

// Initial state factory
export const defineInitialState = (): GameState => ({
  currency: new Decimal(0),
  lifetimeCurrency: new Decimal(0),
  prestigeCurrencies: {},
  generators: {},
  upgradesOwned: [],
  researchNodesOwned: [],
  unlockedMechanics: [],
  paradigmShiftsAchieved: [],
  lastTick: Date.now(),
});

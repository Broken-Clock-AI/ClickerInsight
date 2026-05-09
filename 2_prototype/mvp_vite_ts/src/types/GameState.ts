// @ts-ignore
import Decimal from 'break_infinity.js';

export interface GeneratorState {
  id: string;
  owned: Decimal;
}

export interface GameState {
  currency: Decimal;
  lifetimeCurrency: Decimal;
  prestigeCurrency: Decimal;
  generators: Record<string, GeneratorState>;
  lastTick: number;
}

// Initial state factory
export const defineInitialState = (): GameState => ({
  currency: new Decimal(0),
  lifetimeCurrency: new Decimal(0),
  prestigeCurrency: new Decimal(0),
  generators: {},
  lastTick: Date.now(),
});

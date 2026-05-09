export interface Gdd {
  gameTitle: string;
  core: Core;
  generators: Generator[];
  upgrades: Upgrade[];
  prestige: Prestige;
}

export interface Core {
  currency: Currency;
  manualClickValue: number;
}

export interface Currency {
  name: string;
  initialValue: number;
}

export interface Generator {
  id: string;
  name: string;
  description: string;
  baseCost: number;
  costScaling: number;
  baseProduction: number;
}

export interface Upgrade {
  id: string;
  name: string;
  description: string;
  cost: number;
  unlockCondition: UnlockCondition;
  effect: Effect;
}

export interface UnlockCondition {
  type: 'generator_level' | 'total_currency';
  targetId: string;
  value: number;
}

export interface Effect {
  type: 'multiplier';
  targetId: string;
  value: number;
}

export interface Prestige {
  currencyName: string;
  prestigeRequirement: string;
  formula: string;
  bonusPerPrestige: number;
}

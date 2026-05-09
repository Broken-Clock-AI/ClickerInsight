export interface Gdd {
  meta: Meta;
  playerExperience: PlayerExperience;
  coreLoop: CoreLoop;
  generators: Generator[];
  upgrades: Upgrade[];
  prestige: Prestige;
  paradigmShifts?: ParadigmShift[];
  researchTrees?: ResearchTree[];
  engagementHooks?: EngagementHooks;
  monetization?: Monetization;
}

export interface Meta {
  gameTitle: string;
  gameVersion: string;
}

export interface PlayerExperience {
  numberFormatting: 'scientific' | 'standard';
  uiDirectives: {
    showProductionRates: boolean;
    showEfficiencyScores: boolean;
    liveSurroundings: boolean;
  };
}

export interface CoreLoop {
  primaryCurrency: {
    id: string;
    name: string;
    initialValue: number;
  };
  manualClickValue: {
    baseValue: number;
  };
}

export interface Generator {
  id: string;
  name: string;
  description: string;
  nodeType: 'source' | 'pool' | 'converter' | 'drain' | 'gate'; // GEEVO-2026
  baseCost: number;
  costScaling: number;
  output: GeneratorOutput;
  milestoneBonuses?: MilestoneBonus[];
  claimId?: string; // Traceability to HFS v2.1 Claim Matrix
}

export interface GeneratorOutput {
  type: 'currency' | 'generator';
  targetId: string;
  baseRate: number;
}

export interface MilestoneBonus {
  level: number;
  effect: Effect;
  lore?: string;
}

export interface Upgrade {
  id: string;
  name: string;
  description: string;
  cost: number;
  unlockConditions: UnlockCondition[];
  effect: Effect;
  claimId?: string;
}

export interface UnlockCondition {
  type: 'generator_owned' | 'currency_owned' | 'upgrade_owned';
  targetId: string;
  value: number;
}

export interface Effect {
  type: 'multiplier' | 'additive_bonus';
  targetId: string;
  targetProperty?: string;
  value: number;
  duration?: number; // for temporary effects/buffs
  formula?: string; // for dynamic effects
}

export interface Prestige {
  layers: PrestigeLayer[];
}

export interface PrestigeLayer {
  id: string;
  currencyName: string;
  unlockConditions: UnlockCondition[];
  formula: string;
  effect: Effect;
  resetMechanics: string[];
}

export interface ParadigmShift {
  id: string;
  unlockConditions: UnlockCondition[];
  description: string;
  lore: string;
  newMechanicsUnlocked: string[];
}

export interface ResearchTree {
  id: string;
  name: string;
  description: string;
  currencyCostId: string;
  nodes: ResearchNode[];
}

export interface ResearchNode {
  id: string;
  name: string;
  description: string;
  cost: number;
  unlockConditions?: string[]; // IDs of required nodes
  effect: Effect;
}

export interface EngagementHooks {
  offlineProgression: {
    maxTimeSeconds: number;
    efficiency: number;
  };
  randomRewards: RandomReward[];
}

export interface RandomReward {
  id: string;
  type: 'clickable';
  frequencySeconds: number;
  effect: Effect;
  lore?: string;
}

export interface Monetization {
  rewardedAds: RewardedAd[];
}

export interface RewardedAd {
  id: string;
  name: string;
  cooldownSeconds: number;
  effect: Effect;
  lore?: string;
}

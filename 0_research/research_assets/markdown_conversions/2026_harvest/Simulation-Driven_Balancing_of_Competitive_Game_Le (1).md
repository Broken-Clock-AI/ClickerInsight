# Simulation-Driven Balancing of Competitive Game Levels with Reinforcement Learning

## Abstract
Game balancing for non-symmetrical levels is traditionally a manual process. This work frames game balancing as a procedural content generation (PCG) task and proposes an architecture for automatically balancing tile-based levels within the PCGRL framework.

## Architecture
1. **Level Generator:** Constructs a playable level from random noise.
2. **Balancing Agent:** A PCGRL agent that swaps tile positions to adjust the level.
3. **Reward Modeling Simulation:** Heuristic agents play the level multiple times to determine the win rate, which is used to calculate the balancing agent's reward.

## Methodology Improvements
- **Swap-based Representations:** Instead of replacing tiles (which can lead to unplayable states), the agent swaps existing tiles, ensuring robustness.
- **Fairness Metrics:** The reward function is inspired by the "statistical parity" metric from the fair machine learning community.
- **Configurable Balance:** The system can be configured to balance towards equal win rates (b=0.5) or arbitrary target values.

## Key Results
- The swap-based PCGRL method outperformed original PCGRL and hill-climbing baselines.
- The best model achieved a 68% balance rate on generated levels.
- Swapping resource tiles (forest) with blocking elements (stone) was found to have the highest impact on balance.

## Conclusion
Separating level generation and balancing into two subsequent processes allows for effective fine-tuning of existing content. The method is domain-independent and provides empirical evidence of how game systems behave under different tile configurations.

# Personalized Dynamic Difficulty Adjustment – Imitation Learning Meets Reinforcement Learning

## Abstract
This work explores balancing game difficulty using a combination of imitation learning (IL) and reinforcement learning (RL) to challenge players based on their individual behavior.

## Proposed Architecture
The framework uses three agents:
1. **Opponent Agent:** The agent the player currently faces.
2. **Imitation Learning Agent:** Observes the player and learns to replicate their actions.
3. **Reinforcement Learning Agent:** Trained to win against the imitation learning agent.

## Implementation & Evaluation
- **Prototype:** Implemented in the FightingICE framework using the `River` library for IL (adaptive random forest) and `Stable Baselines 3` for RL (Advantage Actor-Critic).
- **Results:** Players reported higher satisfaction (7.0 vs 6.6) when playing against the proposed adaptive model compared to a standard MCTS agent.
- **IL Accuracy:** The imitation agent achieved 82-87% accuracy in predicting player actions.

## Conclusion
The combination of IL and RL results in a personalized DDA system that requires minimal manual setup by designers and provides a more engaging experience by adapting to the player's skill level.

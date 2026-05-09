# Level the Level: Balancing Game Levels for Asymmetric Player Archetypes With Reinforcement Learning

## Abstract
Balancing games with asymmetric multiplayer content is challenging. This paper focuses on generating balanced levels for asymmetric player archetypes where the disparity in abilities is balanced entirely through level design.

## Methodology
- **Asymmetric Archetypes:** The study evaluates four archetypes:
    - **Archetype A (Base):** Cannot move over rock/water, wins with 5 points.
    - **Archetype B (Rock Agent):** Can cross rock tiles.
    - **Archetype C (Handicap Agent):** Moves every second turn.
    - **Archetype D (Food Agent):** Wins with 3 or 4 points instead of 5.
- **Approach:** Uses the Procedural Content Generation via Reinforcement Learning (PCGRL) framework to fine-tune existing levels.
- **Action Space:** Improved by reducing the swap-wide representation, leading to faster convergence.

## Key Findings
- PCGRL outperformed random search and hill-climbing baselines in balancing asymmetric setups.
- The greater the initial disparity in strength between archetypes, the more training steps were required for convergence.
- Levels can be balanced by strategically placing resources or separating players to mitigate handicaps.

## Conclusion
Reinforcement learning is an effective tool for balancing asymmetric games through level design, though it can sometimes exploit "unintended" balance states like draws where neither player can win.

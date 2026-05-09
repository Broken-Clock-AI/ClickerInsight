# RuleSmith: Multi-Agent LLMs for Automated Game Balancing

## Abstract
RuleSmith is a framework that achieves automated game balancing by leveraging multi-agent LLMs, a game engine, and Bayesian optimization.

## How RuleSmith Works
1. **LLM Self-Play:** Multi-agent LLMs perform zero-shot self-play by reading natural-language rulebooks and generating actions for game states.
2. **Evaluation:** Multiple self-play trajectories yield win rates and balance indicators.
3. **Bayesian Optimization:** Searches the high-dimensional rule space for balanced configurations, using acquisition-based adaptive sampling to allocate resources efficiently.

## Case Study: CivMini
- **Game:** A simplified civilization-style strategy game with asymmetric factions (Empire vs. Nomads).
- **Tuning:** RuleSmith optimized 12 parameters governing economy, combat, production, and scoring.
- **Results:** Converged to highly balanced configurations (near 50/50 win rates) and provided interpretable rule adjustments.

## Key Contributions
- Demonstrates executable self-play from natural-language rulebooks without specific training.
- Combines LLM reasoning with Bayesian optimization for sample-efficient rule search.
- Provides a scalable approach for balancing complex, rule-driven multi-agent environments beyond games (e.g., economic modeling, policy design).

## Conclusion
RuleSmith offers a new paradigm for automated design tools, treating LLMs as flexible evaluators to navigate complex strategic landscapes.

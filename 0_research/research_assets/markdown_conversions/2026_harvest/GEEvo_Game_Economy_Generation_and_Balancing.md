# GEEvo: Game Economy Generation and Balancing with Evolutionary Algorithms

## Abstract
Game economy design significantly shapes player experience. This paper proposes GEEvo (Game Economy Evolution), a framework to generate and balance graph-based game economies using evolutionary algorithms.

## The GEEvo Process
1. **Generator:** An evolutionary algorithm for creating random but valid game economy graphs.
2. **Balancer:** An evolutionary algorithm to balance graph-based game economies by optimizing weights towards specific objectives (e.g., damage dealt over time).

## Framework Details
- Economies are modeled as directed graphs with five node types: Source, Random Gate, Pool/Fixed Pool, Converter, and Drain.
- The system is "simulation-driven," calculating fitness based on multiple simulation runs.

## Case Study
- The framework was used to balance the damage output of a mage and an archer class to ensure equal damage output in the same time frame.
- Results showed that GEEvo can effectively optimize weights to achieve comparable performance across different character designs.

## Conclusion
GEEvo provides a lightweight and flexible framework for game designers to automate the complex task of economy balancing, especially in the early stages of development.

# Math Ledger (Quantitative Research)
*Formal Models and Formulae for Idle Game Balancing*

## 1. Economic Fundamentals

### 1.1 Item Costing (Exponential Growth)
The standard cost model for idle games where supply is "virtually" limited by the algorithm.
**Formula:** $C_n = C_1 \cdot \alpha^{n-1}$
*   $C_n$: Cost of the $n$-th unit.
*   $C_1$: Base cost of the first unit.
*   $\alpha$: Multiplier (Growth rate). Standard value: $1.15$.
*   **Source:** DEMAINE-2018

### 1.2 Global Stopping Condition (The Payback Threshold)
Defines the point where buying another upgrade is mathematically inferior to simply waiting for the goal.
**Formula:** $G > \frac{M \cdot x_i}{y_i} - x_i$
*   $G$: Current generation rate.
*   $M$: Target cookie goal.
*   $x_i$: Rate increase of item $i$.
*   $y_i$: Current cost of item $i$.
*   **Context:** If this inequality holds, enter the "Waiting Phase" immediately.
*   **Source:** DEMAINE-2018

---

## 2. Optimization Metrics

### 2.1 Efficiency Score (The Greedy Metric)
Used to determine the locally optimal next purchase.
**Formula:** $E_i = \frac{y_i}{x_i} + \frac{y_i}{G}$
*   $y_i/x_i$: "Payback time" once purchased.
*   $y_i/G$: "Waiting time" to afford the item.
*   **Decision Rule:** Always purchase the item with the **lowest** $E_i$.
*   **Source:** DEMAINE-2018

### 2.2 Transition Threshold (2-Item Fixed Cost)
Determines when to stop buying tier 1 and start buying tier 2.
**Formula:** $T = \frac{y_2 - y_1}{y_1/x_1 - y_2/x_2}$
*   $T$: Generation rate threshold.
*   **Decision Rule:** If $G < T$, buy Tier 1. If $G > T$, buy Tier 2.
*   **Source:** DEMAINE-2018

---

## 3. Pacing & Time Estimation

### 3.1 Time to Goal (1-Item Approximation)
Estimates the total time needed to reach goal $M$ using one optimal generator.
**Formula:** $T_{total} \approx \frac{y}{x} \ln(\frac{M \cdot x}{y}) + 1$
*   **Source:** DEMAINE-2018

### 3.2 Approximation Ratio (Greedy vs. Optimal)
The Efficiency Score Greedy Solution is an approximation algorithm.
**Ratio:** $1 + O(\frac{1}{\log M})$
*   **Implication:** For large $M$, the greedy approach is indistinguishable from the global optimum.
*   **Source:** DEMAINE-2018

---

## 4. Complexity & Constraints

### 4.1 Reach-Goal NP-Hardness
*   **M-version:** Reaching $M$ cookies is polynomial-time solvable (via DP).
*   **R-version:** Reaching a rate $R$ is **Weakly NP-hard** (reduction from Partition).
*   **Discrete Timesteps:** The discrete version is **Strongly NP-hard** (reduction from 3-Partition).
*   **Source:** DEMAINE-2018

---

## 5. System Interactions (Mathematical)

### 5.1 Initial Cookie Injection ($z > 0$)
If starting with a large surplus of cookies $z$:
*   **Rule:** Spend all $z$ immediately at $t=0$ on the most efficient items until $z < y_{min}$ or the stopping condition is met.
*   **Source:** DEMAINE-2018

---

## 6. Multi-Resource & Systemic Models

### 6.1 Resource Capacity (The Storage Constraint)
Most automated resources are capped by "Entities" (Storage Buildings).
**Rule:** $Current \le Capacity$. If $Current = Capacity$, excess production is wasted.
**Decision Rule:** Pacing shifts from "Production Optimization" to "Storage Expansion" when the "Time to Cap" is shorter than the desired idle period.
**Source:** ALHARTHI-2017

### 6.2 Population Drain (Consumption)
Resources consumed by game entities (e.g., Kittens consuming Catnip).
**Formula:** $Net_{rate} = Production - Consumption$
**Condition:** If $Net_{rate} < 0$ and $Current = 0$, entities are "starved" or removed.
**Source:** ALHARTHI-2017

### 6.3 Happiness Multiplier (The Luxury Good Effect)
Rare resources boost global production via a "Happiness" variable.
**Formula:** $Production_{effective} = Production_{base} \cdot (1 + Bonus_{happiness})$
**Source:** ALHARTHI-2017

### 6.4 Crafting Effectiveness (Yield Bonus)
Secondary buildings (Workshops) increase the yield of resource conversion.
**Formula:** $Yield = Base \cdot (1 + (Count_{workshops} \cdot Bonus_{per\_workshop}))$
*   Standard bonus: $+6\%$ per Workshop.
*   **Source:** ALHARTHI-2017

### 6.5 Reset Bonuses (Paragon/Karma)
Meta-progression variables that persist across runs.
**Paragon Effect:** $+0.1\%$ Production AND $+0.1\%$ Storage Capacity per point.
**Karma Effect:** Increases global Happiness bonus.
**Source:** ALHARTHI-2017

---

## 7. AI-Driven Optimization (Modern)

### 7.1 Bayesian Design Search
High-dimensional rule space optimization using LLM self-play as the evaluation function.
**Method:** Bayesian Optimization with Acquisition-based Adaptive Sampling.
**Goal:** Minimize $|\text{Target\_Outcome} - \text{Simulated\_Outcome}|$ across $k$ parameters.
**Source:** RULESMITH-2026

### 7.2 Zero-Shot Design Validation
The ability of an LLM agent to execute a natural-language rulebook to validate balance without training.
**Rule:** $\text{State}_{t+1} = \text{LLM}(\text{Rules}, \text{State}_t, \text{Action})$.
**Source:** RULESMITH-2026

---

## 8. Structural Economy Modeling

### 8.1 Graph-Based Economy Nodes
Modern economies are modeled as directed graphs $G = (V, E)$.
**Node Types ($V$):**
1.  **Source:** Generates resources (e.g. Click, Auto-generator).
2.  **Pool (Storage):** Holds resources; subject to capacity caps.
3.  **Converter:** Trades $X$ for $Y$ at a specific weight/ratio.
4.  **Drain:** Permanently removes resources (e.g. consumption, maintenance).
5.  **Random Gate:** Multiplies flow by a probability $p$ (e.g. rare spawns).
**Source:** GEEVO-2026

### 8.2 Simulation-Driven Fitness
Optimizing economy weights $W$ by minimizing the delta from target objectives.
**Fitness Function:** $F(W) = \sum |T_i - S_i(W)|$
*   $T_i$: Target metric (e.g. "Total resources at $t=3600$").
*   $S_i(W)$: Simulated outcome with weights $W$.
**Source:** GEEVO-2026

---

## 9. Monetization & Retention Benchmarks (2025-2026)

### 9.1 Ad-Based Revenue (ARPU)
*   **Hypercasual Baseline:** ~$0.86 ARPU.
*   **Hybrid Casual (Idle/Merge):** ~$14.83 ARPU (High-end), ~$5.00 (Standard).
*   **Source:** APPODEAL-2025

### 9.2 Rewarded Video (RV) Engagement
Frequency of ad views per user per lifecycle.
*   **Idle Games:** ~73.2 RVs per user.
*   **Merge 3 Games:** ~101.5 RVs per user.
*   **Strategy:** Idle loops must provide "RV-worthy" boosters at a frequency that matches these engagement targets without breaking progression.
*   **Source:** APPODEAL-2025

# Document Profile: The Math of Idle Games, Part II

*   **Source:** `blog_kongregate_com_the_math_of_idle_games_part_ii_.md`
*   **Original URL:** `https://blog.kongregate.com/the-math-of-idle-games-part-ii/`

---

### **Abstract/Executive Summary**

This article explores an alternative mathematical model for idle game progression, moving beyond the standard "Cookie Clicker" model where all generators produce a single primary currency. It proposes a "derivative-based" system where generators produce *other generators* in a cascading chain. The author explains how this system, where each generator tier represents the rate of change (a derivative) of the tier below it, mathematically approaches exponential growth (`e^x`) without being purely exponential. This creates a satisfying feeling of nested progression and solves the problem of costs eventually outpacing production. The article uses "Derivative Clicker" and "Shark Game" as examples and discusses design solutions, like tier boosts based on *purchased* units, to keep lower-level generators relevant even when they are being generated for free in massive quantities.

---

### **Key Sections**

1.  **Introduction:**
    *   Recap of Part I (standard exponential/polynomial growth models).
    *   Introduction of the core question: What if generators produced other generators instead of currency?

2.  **The Derivative Model Explained:**
    *   Visualizing the cascade: Gen 2 produces Gen 1, which produces Currency.
    *   Calculus Analogy: Explains how each generator tier acts as a derivative of the next, and how integrating up the chain leads to polynomial growth functions (`x^n/n!`).
    *   Approaching Exponential Growth: Demonstrates how summing the outputs of an infinite number of these generator tiers forms a Taylor Series that equals `e^x`.

3.  **Practical Application & Examples:**
    *   **"Derivative Clicker" Analysis:** Cites this game as a clear implementation of the derivative model.
    *   **"Shark Game" Mention:** Notes its use of generators that produce other generators.

4.  **Solving Design Challenges:**
    *   **The Relevancy Problem:** Addresses why players would buy a lower-tier generator when it's being produced for free by a higher tier.
    *   **Proposed Solution (from Derivative Clicker):** Implement "tier boosts" where purchasing a generator provides a permanent boost to that entire tier's production, creating a separate incentive for manual purchases.

5.  **Conclusion & Encouragement:**
    *   Advocates for designers to experiment with hybrid models and complex generator interdependencies.
    *   Final message is to "Draw lines between them. See what happens!" to foster innovation in the genre.

---

### **Document Type**

*   Game Design Analysis / Technical Blog Post

---

### **Core Keywords**

*   Derivative-based growth
*   Idle games
*   Incremental games
*   Game mathematics
*   Progression systems
*   Exponential growth
*   Polynomial growth
*   Calculus
*   Generators
*   Tier boosts
*   Game balance

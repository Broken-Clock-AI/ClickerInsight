# Document Profile: Math — the backbone of Idle Games (Part 1)

*   **Source:** `medvescekmurovec_medium_com_math_the_backbone_of_idle_games_part_1_f46b54706cf1.md`
*   **Original URL:** `https://medvescekmurovec.medium.com/math-the-backbone-of-idle-games-part-1-f46b54706cf1`

---

### **Abstract/Executive Summary**

This article serves as an introduction to the fundamental mathematical principles that underpin idle games, with a focus on exponential growth. It traces the genre's history from *Progress Quest* to modern titles like *AdVenture Capitalist* and *Cookie Clicker*. The core game loop of idle games is described: perform actions to generate currency, spend currency on upgrades/generators, hit a "progression wall," and then "prestige" for permanent powerful upgrades to restart and progress further. The article defines key game elements (clicking, currency, upgrades, generators, multipliers, prestige, run) and explains the crucial balance between cost growth (typically faster, e.g., exponential) and income growth (typically slower, e.g., polynomial). It illustrates function growth comparisons (linear vs. polynomial vs. exponential) and discusses big number notations (arbitrary vs. scientific). A practical example, "Woodchuck Idle," demonstrates how exponential cost increases ensure a progression wall, even with linear income growth.

---

### **Key Sections**

1.  **Introduction:**
    *   Defines idle/clicker games and their goal of amassing wealth.
    *   Brief history of the genre, mentioning key titles.
    *   Highlights math as the backbone of these games.

2.  **Game Loop:**
    *   Describes the basic loop: action -> currency -> upgrades/generators -> progression wall -> prestige/New Game Plus -> restart with permanent upgrades.
    *   Focuses on games without specific victory conditions, emphasizing constant progression.

3.  **Patterns and Building Blocks:**
    *   **Clicking:** Initial interaction, often automated later.
    *   **Currency:** Primary resource and goal.
    *   **Upgrades:** Improve currency production.
    *   **Generators:** Produce currency over time, can include "generator generators."
    *   **Multipliers/Bonuses:** Increase production, often from achievements or rewarded ads.
    *   **Prestige/Ascension/New Game Plus:** Resets progress for powerful permanent upgrades.
    *   **Run:** Gameplay session between prestiges.

4.  **Math Basics:**
    *   **Developer's Goal:** Balance between upgrade costs and income increase.
    *   Costs must grow faster than income to create progression walls.
    *   **Function Growth:** Explains linear, polynomial, and exponential growth, demonstrating how faster-growing functions eventually overtake slower ones (e.g., exponential > polynomial > linear).
    *   Introduces the concept of ignoring slower-growing parts of complex equations.
    *   Mentions "The Big O notation" for detailed function growth.

5.  **Big Number Notations:**
    *   Discusses methods for displaying large numbers: arbitrary notation (e.g., k, M, B, T, a, b) and Scientific/E notation (e.g., `xen`).

6.  **Example: Woodchuck Idle:**
    *   A simple game with one goal: gather wood.
    *   Two upgrades: "Strong Tooth" (per click) and "Hire a Woodchuck" (per second).
    *   Demonstrates how exponential cost increases (e.g., 15% or 7% per level) lead to progression walls, even with linear income increases.
    *   Briefly mentions rounding costs.

---

### **Document Type**

*   Game Design Blog Post / Technical Article (Mathematics of Games)

---

### **Core Keywords**

*   Idle games
*   Incremental games
*   Game mathematics
*   Exponential growth
*   Polynomial growth
*   Game loop
*   Prestige mechanic
*   Generators
*   Upgrades
*   Progression wall
*   Big numbers notation
*   Game balance
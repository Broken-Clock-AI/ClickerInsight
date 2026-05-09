# Distilled Design Principles for Incremental Games
_A synthesis of the core concepts from "The Compounding Illusion" tome._

This document distills the foundational knowledge from our research into actionable principles for designing a rich, engaging, and ethical incremental game. It will serve as the basis for our `GameDesignDocument_v2_schema.json`.

---

### 1. Core Loop & Mathematical Principles

- **The Core Loop:** A repeating cycle of **Accumulate -> Invest -> Automate**. This is the fundamental engine of progression.
- **The Core Seesaw:** A critical balance where **Upgrade Costs must grow exponentially faster than Production**. This creates the fundamental tension that necessitates prestige.
- **Growth Functions:**
    - **Polynomial Growth:** Used for production rates (`x^n`).
    - **Exponential Growth:** Used for costs (`c^x`). This mathematical imbalance is the core challenge.
- **Prestige Mechanics:**
    - **Purpose:** To reset progress in exchange for a permanent, powerful boost (the "ladder climbing effect"). It is the solution to the Core Seesaw.
    - **Calculation:** Often uses **fractional exponents** (`total_currency ^ 0.5`) to convert large numbers into a manageable prestige currency.
    - **Architectures:** Can be based on **lifetime stats** (encourages pushing runs) or **since-reset stats** (encourages optimal-length runs).
- **Big Number Notation:** Must use **Scientific/E-notation** for late-game clarity and to prevent overflow.

---

### 2. Advanced Mechanics & Systems

- **Generator Ecosystems:**
    - **Trivial Dominance (To Avoid):** The newest generator should not always be the most efficient.
    - **Shifting Priorities (To Implement):** Balancing must create situations where older generators become temporarily more valuable, forcing strategic, non-linear choices. This is achieved via milestone bonuses.
    - **Derivative-Based Growth:** Advanced model where high-tier generators produce lower-tier ones, creating a cascading `e^x` growth model and keeping all generators relevant.
- **Progression Pacing:**
    - **Bumpy Progression:** The player's journey should alternate between fast growth and slow plateaus/walls. This is more engaging than a smooth, predictable curve.
    - **Paradigm Shifts:** At key milestones, the game should introduce entirely new mechanics or systems, creating a "joy of discovery" and fundamentally altering gameplay. This is the primary vehicle for the game's narrative.

---

### 3. Player Psychology & Engagement

- **Interpassivity:** The core psychological appeal. Players derive pleasure from a system that "plays for them," making progress in their absence. The design must respect and reward this disengagement.
- **Operant Conditioning & Habit Formation:**
    - **Variable Reward Schedules:** Unpredictable rewards (e.g., clickable "golden cookies," rare drops) are more compelling than fixed ones.
    - **Daily Hooks:** Daily quests, login bonuses, and capped offline earnings (e.g., max 4 hours of income) create a mild, ethical FOMO that encourages regular check-ins.
- **The First Five Minutes:** The initial experience must be fast, rewarding, and clearly demonstrate the "number go up" appeal to ensure player retention.
- **The Player as Planner:** The core gameplay is not clicking, but **optimization**. The UI/PX should empower the player to make strategic decisions.

---

### 4. Narrative & Player Experience (PX)

- **Narrative Through Abstraction:** The story is told through the gradual unfolding of the game's mechanics. Paradigm shifts are the "chapters" of this story.
- **Ludic Efficiency:** The UI must be clean, intuitive, and efficient. It should help players make informed decisions quickly without overwhelming them.
    - **Cognitive Offloading:** Provide tools like tooltips, clear metrics (`/sec`), and potential future-state calculations to help players plan.
- **Live Surroundings:** The game should feel alive. Visual feedback, animations, and a sense of bustling activity are crucial to make the abstract numbers feel tangible and rewarding.
- **Meaningful Choice:** Avoid single, "correct" upgrade paths. At any point, the player should have several valid strategic options to consider.

---

### 5. Ethics & Monetization

- **Calm Technology:** The game should exist in the periphery of a player's life, not demand constant attention. Avoid intrusive notifications and high-stress, timed events.
- **Player-Friendly Design (PFD):** A non-negotiable framework.
    - **Respect Player Time:** Don't force play. Reward taking breaks.
    - **Respect Player Wallet:** Don't force spending. No paywalls. F2P players must be able to complete all content.
    - **Avoid Pay-to-Win:** IAPs should offer convenience or cosmetics, not insurmountable advantages.
- **Hybrid Monetization Model:** The most effective and ethical model combines:
    - **Rewarded Ads (Player-Initiated):** The preferred ad format. Players choose to watch an ad for a clear, valuable reward (e.g., a temporary production boost).
    - **In-App Purchases (IAPs):** For non-essential permanent benefits (e.g., remove banner ads, cosmetic changes) or convenience items (e.g., "time skips").

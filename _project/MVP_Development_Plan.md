# Plan of Action: Developing a "Killer Incremental" MVP

This document outlines the phased approach to translate the foundational research from the `final_tome` into a tangible, playable, and well-designed Minimum Viable Product (MVP). We will follow this charted course to ensure development is both rapid and directly informed by our synthesis.

## Phase 1: Foundation - From Research to Blueprint

The goal of this phase is to transform our comprehensive research into a structured, actionable engineering blueprint. This is the most critical step to ensure we build a "killer" incremental game, not just a functional one.

### Step 1.1: Create the Game Design Document (GDD)

We will deconstruct the `final_tome` from a descriptive text into a structured, queryable GDD. This document will serve as the single source of truth for all game mechanics, balancing, and design principles.

*   **Action:** Create `design/GameDesignDocument_schema.json` to define the structure of our GDD.
*   **Action:** Systematically read the `final_tome` and populate `design/GameDesignDocument.json` with concrete data, formulas, and rules based on the defined schema.

### Step 1.2: Define the Technical Specification

With the GDD as our guide, we will outline the technical plan for the MVP.

*   **Action:** Create `development/tech_spec.md`.
*   **Content:**
    *   **Tech Stack:** Propose a minimal-friction stack for rapid prototyping (e.g., HTML, CSS, Vanilla JavaScript).
    *   **Project Structure:** Define the file and directory layout.
    *   **Data Model:** Outline the core JavaScript object that will manage the player's state (currency, generators, upgrades, etc.).
    *   **Game Loop:** Specify the main game loop logic (e.g., using `setInterval` for updates).

## Phase 2: Implementation - Building the Core Experience

This phase focuses on writing the code to create a playable, if minimal, version of the game based on the specifications from Phase 1.

### Step 2.1: Set Up the Project Environment

*   **Action:** Create the initial project scaffolding: `index.html`, `app/css/style.css`, and `app/js/app.js`.

### Step 2.2: Implement the Core Loop

*   **Action:** Write the initial JavaScript code to bring the game's core to life.
    *   Implement manual currency generation (the "clicker").
    *   Implement the ability to purchase the first generator.
    *   Develop the UI to display currency, production rates, and generator counts.

### Step 2.3: Implement Progression and Scaling

*   **Action:** Build out the systems that create long-term engagement, directly referencing the GDD for balancing.
    *   Add 2-3 additional generator tiers.
    *   Implement the exponential cost scaling formulas.
    *   Implement a basic upgrade system that provides multipliers.

### Step 2.4: Implement the Prestige System

*   **Action:** Implement the most critical long-term loop from our research.
    *   Code the prestige currency calculation based on the formula in the GDD.
    *   Implement the game reset functionality.
    *   Apply the permanent bonuses that prestige provides.

## Phase 3: Polish and Refinement

With the core mechanics in place, this phase focuses on adding the experiential layers that elevate the game from a functional prototype to an engaging experience.

### Step 3.1: Enhance the User Experience (UX)

*   **Action:** Add feedback and "game feel" based on principles from the `final_tome`.
    *   Implement visual feedback for clicks, purchases, and unlocks.
    *   Add animations or other "live surroundings" elements to make the game feel dynamic.

### Step 3.2: Implement Retention Hooks

*   **Action:** Add mechanics designed to bring players back.
    *   Implement offline progress calculation.
    *   Add a simple daily reward or login bonus.

Upon completion of this plan, we will have a playable MVP that is not only functional but is built upon a solid foundation of best-in-class design principles.

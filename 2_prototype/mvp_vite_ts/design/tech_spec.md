# Technical Specification for "The Compounding Illusion" MVP

This document outlines the technical plan for the Minimum Viable Product (MVP), based on the `GameDesignDocument.json`.

## 1. Tech Stack

For rapid prototyping and maximum accessibility, the MVP will be built using a minimal-friction web stack:

*   **HTML:** For the core structure and content.
*   **CSS:** For styling and layout.
*   **JavaScript (Vanilla):** For all game logic, DOM manipulation, and state management. No external frameworks or libraries will be used for the initial MVP to keep it lightweight and focused.

## 2. Project Structure

The project will follow a simple, clear directory structure:

```
.
├── index.html
├── design/
│   ├── GameDesignDocument.json
│   └── GameDesignDocument_schema.json
├── development/
│   └── tech_spec.md
└── app/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

*   `index.html`: The main entry point of the application.
*   `design/`: Contains the GDD and its schema.
*   `development/`: Contains technical planning documents.
*   `app/css/style.css`: All styles for the user interface.
*   `app/js/app.js`: The single source for all game logic.

## 3. Data Model (Player State)

The core of the game will be managed by a single JavaScript object, referred to as `gameState`. This object will hold all player-specific data and will be the single source of truth for the UI.

```javascript
let gameState = {
    cogs: 0,
    cogsPerSecond: 0,
    
    generators: {
        gen01: {
            level: 0,
            production: 0
        },
        gen02: {
            level: 0,
            production: 0
        },
        gen03: {
            level: 0,
            production: 0
        }
    },
    
    prestige: {
        chronoShards: 0,
        bonus: 1 // Starts at 1 (100% or no bonus)
    },
    
    // To track stats for prestige calculation
    stats: {
        totalCogsProduced: 0
    }
};
```

## 4. Game Loop

The main game loop will be responsible for updating the `gameState` and re-rendering the UI. It will be powered by `setInterval`.

*   **Frequency:** The loop will run at a fixed interval, likely 10 times per second (every 100ms), to provide a smooth and responsive experience.
*   **Logic:**
    1.  Calculate `cogsPerSecond` based on the production of all generators and all active multipliers (including prestige bonuses).
    2.  Increment the player's `cogs` by the `cogsPerSecond` divided by the loop frequency.
    3.  Update the UI to reflect the new `cogs` count and `cogsPerSecond`.
    4.  Check for any newly unlocked upgrades and update the UI accordingly.

```javascript
// Main Game Loop
function gameLoop() {
    // 1. Calculate production
    let currentCps = 0;
    // ... logic to calculate CPS from gameState.generators and gameState.prestige.bonus ...
    gameState.cogsPerSecond = currentCps;
    
    // 2. Increment resources
    gameState.cogs += gameState.cogsPerSecond / 10; // Assuming 10 ticks per second
    gameState.stats.totalCogsProduced += gameState.cogsPerSecond / 10;

    // 3. Update UI
    updateUI();
}

// Start the loop
setInterval(gameLoop, 100); // 100ms = 10 times per second
```

# 2. Prototype Phase

The practical application of the HFS (High-Fidelity Synthesis) research. This directory contains the functional game engine and formal design specifications.

## Contents
- **`mvp_vite_ts/`**: A modern web-based incremental engine built with React, TypeScript, and Zustand.
    - Uses `break_infinity.js` for high-precision large numbers.
    - Implements a formal "Generator-to-Generator" production model.
- **Design Specifications:** Found within `mvp_vite_ts/data/` and `mvp_vite_ts/design/`.
    - `GameDesignDocument_v5.json`: The current active configuration.
    - `tech_spec.md`: Architectural overview of the engine.

## Current Focus
We are currently hardening the GDD schema into a formal YAML specification to support **Agent-Based Simulation** for long-term balance verification.

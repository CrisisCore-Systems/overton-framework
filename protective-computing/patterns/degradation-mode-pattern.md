# Degradation Mode Pattern

## Problem Statement
Under degraded conditions, complex interfaces and fragile flows increase cognitive load and error likelihood.

## Context
Applies when:
- users can be in cognitive overload or crisis conditions.

## Constraints
- Reduced capability modes MUST preserve essential utility.
- Mode transitions MUST be legible and reversible.

## Implementation Template
- Define explicit degraded modes (e.g., reduced UI density, fewer prompts).
- Ensure deterministic routing under degraded conditions.
- Suppress non-essential interruptions.

## Failure Modes
- False activation restricts user unexpectedly
- Missed activation fails to protect

## Tradeoffs
- Additional state and testing complexity

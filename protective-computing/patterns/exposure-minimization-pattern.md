# Exposure Minimization Pattern

## Problem Statement
Unnecessary data transmission, metadata emission, and logging increase exposure surface during Vulnerability States.

## Context
Applies when:
- systems handle sensitive or high-stakes user data.

## Constraints
- Telemetry MUST NOT be ambient by default.
- Remote infrastructure MUST be treated as compellable.

## Implementation Template
- Keep sensitive content on-device by default.
- Minimize metadata emission (events, identifiers, timestamps).
- Avoid logging reconstructive content.
- Require explicit user initiation for any remote transfer.

## Failure Modes
- Debug logging leaks sensitive content
- Analytics creates behavioral reconstruction pathways

## Tradeoffs
- Reduced observability
- Harder remote support and incident triage

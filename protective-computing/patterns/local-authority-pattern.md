# Local Authority Pattern

## Problem Statement
Systems that require remote infrastructure for essential utility can deny users access at the moment it matters (connectivity loss, service outage, administrative denial).

## Context
Applies when:
- essential read/write tasks must remain available under degraded connectivity and institutional latency.

## Constraints
- Sensitive data SHOULD remain locally available.
- Remote services MUST be treated as unavailable or compellable.

## Implementation Template
- Store critical state locally.
- Sync is OPTIONAL for core operation.
- Encrypt sensitive state at rest.
- Provide explicit, user-controlled export pathways.
- Implement offline-first reconciliation (queue + retry + conflict handling).

## Failure Modes
- Local storage corruption or quota exhaustion
- Divergent states across devices
- Clock skew impacts reconciliation

## Tradeoffs
- Increased local complexity
- Potential sync conflicts and storage overhead

# Reversible State Pattern

## Problem Statement
Irreversible operations executed during Vulnerability States can cause permanent harm (data loss, lockout, unrecoverable permissions).

## Context
Applies when:
- destructive or high-impact actions exist (delete, revoke access, permanent submission, irreversible exports).

## Constraints
- Restore MUST be possible within a bounded restoration window.
- Confirmation friction SHOULD be proportional to impact.

## Implementation Template
- Use append-only or non-destructive persistence (soft delete + tombstones).
- Provide a restoration window and visible recovery UI.
- Delay or buffer irreversible actions when feasible.

## Failure Modes
- Recovery mechanism becomes a coercion surface
- Excessive retention violates minimization requirements

## Tradeoffs
- Storage overhead
- Complex lifecycle management for retention and purge

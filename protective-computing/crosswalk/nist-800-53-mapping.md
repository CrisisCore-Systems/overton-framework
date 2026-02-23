# Protective Computing ↔ NIST SP 800-53 Crosswalk (Draft)

## Status
This document is **informative** and provides a mapping aid. It does not change Core requirements.

## Mapping Table (Skeleton)

| Protective Principle | NIST 800-53 Control Family / Example | Notes |
| --- | --- | --- |
| Local Authority | SC (System and Communications Protection) / SC-28 | Protect local confidentiality and reduce remote dependency where feasible. |
| Exposure Surface Minimization | AC (Access Control) / AC-3 | Least privilege and minimized access paths. |
| Reversibility Under Degraded Operation | CP (Contingency Planning) / CP-10 | Recovery mechanisms and bounded restoration. |
| Failure Containment | SI (System and Information Integrity) / SI-13 | Predictable failure behavior and containment. |
| Asymmetric Power Defense | PL / PM (Program Management) | Governance and portability controls vary by system scope. |

## Notes
- This crosswalk MUST be validated against the system’s explicit threat model.

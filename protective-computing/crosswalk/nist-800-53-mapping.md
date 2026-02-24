
# Crosswalk — Protective Computing Core v1.0.0 → NIST SP 800-53 (Rev. 5)

This crosswalk maps selected Protective Computing Core requirements and principles to **relevant NIST SP 800-53 (Rev. 5)** control families/controls.
It is **not** a claim of NIST compliance; it is a traceability aid for risk and control discussions.

## High-signal mappings (initial set)

| Protective Computing (PC) concept | NIST 800-53 control(s) | Why this maps (conservative) |
|---|---|---|
| Local Authority (default local control, minimal remote dependency) | **SC-28** (Protection of Information at Rest) | Emphasizes protecting sensitive information stored locally under the user's authority. |
| Exposure Surface Minimization (reduce data leaving the local boundary) | **PT-2** (Authority to Process Personally Identifiable Information) / **AR-2** (Privacy Impact and Risk Assessment) | Exposure minimization aligns with privacy governance that constrains collection/processing and assesses risk from processing choices. |
| “By default” least exposure (off-by-default analytics / optional services gated) | **CM-7** (Least Functionality) | Minimizing enabled functionality and optionalizing non-essential data flows aligns with least-functionality defaults. |
| Explicit degradation modes and preserved essential utility in degraded conditions | **CP-2** (Contingency Plan) / **CP-10** (System Recovery and Reconstitution) | Degradation-mode behavior and preserving essential utility are aligned with planning for degraded operation and recovery behavior. |
| Bounded reversibility / recovery window for high-impact destructive operations (where security allows) | **CP-10** (System Recovery and Reconstitution) / **SI-12** (Information Management and Retention) | Reconstitution concepts and controlled retention/destruction behavior map to recovery and predictable lifecycle handling. |
| Coercion-resistance / safety under asymmetric power | **PL-8** (Information Security Architecture) / **PM-11** (Mission/Business Process Definition) | Architecture-level controls and mission/process definitions support designing for hostile or coercive contexts (conservative mapping). |
| Evidence / testability model for conformance claims | **CA-2** (Control Assessments) / **CA-7** (Continuous Monitoring) | A defined evidence model supports assessment and ongoing verification. |

## Notes / cautions
- NIST 800-53 is an organizational control catalog. Protective Computing targets system-level design behavior under vulnerability; mappings are therefore approximate and should be refined per system context.
- Where Protective Computing recommends irreversibility protections, systems must still preserve security invariants (e.g., brute-force resistance) when designing bounded reversibility.

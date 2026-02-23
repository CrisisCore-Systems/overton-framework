# Protective Computing Core Specification v1.0

## 1. Abstract (Informative)
Protective Computing defines requirements for software systems operating in contexts where user agency is degraded and system failure can plausibly produce health, safety, or rights harms. This Core Specification defines vocabulary, a neutral threat model, a conformance model, a testability/evidence model, and numbered normative requirements intended to preserve **Local Authority**, minimize **Exposure Surface**, and reduce **irreversible** outcomes under degraded operation.

## 2. Document Status and Scope (Normative)
2.1 This document is **Protective Computing Core v1.0**.

2.2 This document is the authoritative reference for **Core** conformance claims.

2.3 This Core applies to systems where failure can plausibly produce health, safety, or rights harms. Systems outside this scope MAY adopt these requirements as best practice but MUST NOT claim Core conformance unless they meet the conformance model in Section 6.

2.4 Normative language is defined in [normative-language.md](normative-language.md).

## 3. Normative References (Normative)
3.1 RFC 2119 and RFC 8174 are normative for interpreting capitalized requirement keywords.

## 4. Terminology (Normative)
4.1 Terms used by this specification are defined in [glossary.md](glossary.md).

4.2 A conforming system MUST define (and publish as an implementation artifact) which data and functions are treated as **critical** for Essential Utility and Local Authority.

## 5. Threat Model (Normative)
5.1 Systems claiming conformance MUST define an explicit threat model that includes, at minimum, the threat classes below.

5.2 Connectivity Degradation
- Loss or intermittency of network transport (including high latency, partial reachability, captive portals, or intermittent power).

5.3 Cognitive Degradation
- Reduced user capacity for complex interaction (including limited attention, memory, comprehension, or time budget).

5.4 Environmental Instability
- Operation under unsafe or unpredictable physical context (including device inspection risk, limited private time, or observation risk).

5.5 Institutional Latency
- Delay, outage, or discretionary denial in institutional dependencies (vendors, platforms, administrators, or counterparties) that can block Essential Utility.

5.6 Coercive Access
- Forced device access, compelled disclosure, or adversarial oversight by individuals or institutions.

## 6. Conformance Model (Normative)
6.1 A system MAY claim conformance to Protective Computing Core v1.0 only if:
- All requirements labeled **MUST** and **MUST NOT** in Section 7 are satisfied.
- All requirements labeled **SHOULD** in Section 7 are either satisfied or explicitly documented as a deviation with rationale.
- The system publishes a Conformance Matrix per Section 9.
- The system publishes a Threat Model Statement that satisfies Section 5.

6.2 If a system cannot satisfy a **MUST** or **MUST NOT** requirement due to domain constraints, it MUST NOT claim Core conformance. It MAY claim partial alignment and MUST enumerate deviations.

6.3 Claims of conformance MUST state the exact Core version (e.g., “Protective Computing Core v1.0”).

## 7. Core Requirements (Normative)
Each requirement in this section is uniquely identified as **PC-REQ-n**.

### 7.1 Local Authority
PC-REQ-1: Systems MUST preserve user authority over locally stored critical data in the absence of network connectivity.

PC-REQ-2: Systems MUST provide Essential Utility read capability without remote dependency.

PC-REQ-3: Where the domain requires writing during degraded connectivity, systems SHOULD provide Essential Utility write capability offline; if full offline write is infeasible, systems MUST provide local capture-and-queue with non-destructive reconciliation.

### 7.2 Reversibility
PC-REQ-4: Systems SHOULD minimize irreversible state transitions during Vulnerability States.

PC-REQ-5: Systems MUST NOT introduce irreversible loss of locally stored critical data during a Vulnerability State unless explicitly confirmed by the user through a deliberate confirmation step.

PC-REQ-6: Systems MUST provide a bounded restoration window for high-impact operations affecting locally stored critical data.

### 7.3 Exposure Surface Minimization
PC-REQ-7: Systems MUST document their Exposure Surface (data flows, metadata emissions, logs, and external dependencies) as an implementation artifact.

PC-REQ-8: Systems MUST minimize remote transmission of sensitive content and high-risk metadata.

PC-REQ-9: Systems MUST NOT increase Exposure Surface during degraded operation.

### 7.4 Failure Containment
PC-REQ-10: Systems MUST define deterministic behavior for loss of connectivity and loss of external services relevant to Essential Utility.

PC-REQ-11: Systems MUST fail in a manner that contains harm escalation when dependencies degrade.

### 7.5 Degradation Modes
PC-REQ-12: Systems MUST define explicit degradation modes for operation under degraded conditions, including how Essential Utility is preserved.

PC-REQ-13: Degradation mode entry/exit MUST be legible to the user and MUST be reversible.

### 7.6 Asymmetric Power Defense
PC-REQ-14: Systems MUST provide user-controlled export pathways in non-proprietary formats for critical user data.

PC-REQ-15: Systems SHOULD implement coercion-resistance mechanisms appropriate to the platform and domain, or document why such mechanisms are not implemented.

## 8. Testability and Evidence Model (Normative)
8.1 For each PC-REQ requirement, a conforming system MUST provide at least one evidence method in its Conformance Matrix (Section 9).

8.2 Evidence methods MAY include:
- Automated tests (unit/integration/e2e) demonstrating required behavior.
- Static analysis or configuration review.
- Manual test procedures with reproducible steps.
- Architectural documentation pointing to the mechanism that enforces the requirement.

8.3 Evidence MUST be sufficient for an independent reviewer to reproduce the claim.

## 9. Conformance Matrix Template (Normative)
9.1 Conforming systems MUST publish a Conformance Matrix including, at minimum, the columns below.

| Requirement | Status (Yes/No/Partial) | Implementation Location | Evidence | Notes / Deviations |
| --- | --- | --- | --- | --- |
| PC-REQ-1 |  |  |  |  |
| PC-REQ-2 |  |  |  |  |

9.2 “Partial” MUST include a deviation rationale and a description of residual risk.

## 10. Versioning Policy (Normative)
10.1 Protective Computing Core uses semantic versioning:
- **MAJOR**: breaking requirement changes (including requirement removals, weakening MUST/MUST NOT constraints, or materially changing conformance conditions).
- **MINOR**: additive requirements that do not break existing conformance (e.g., new SHOULD requirements or new optional informative guidance).
- **PATCH**: clarifications that do not change the set of conformance obligations.

10.2 Conformance claims MUST cite the full version.

## 11. References (Informative)
- RFC 2119
- RFC 8174


# Crosswalk — Protective Computing Core v1.0.0 → GDPR Principles / Articles

This crosswalk maps Protective Computing Core concepts to **GDPR principles and commonly-relevant articles**.
It is **not** legal advice and **not** a claim of GDPR compliance; it is a traceability aid for privacy-by-design discussions.

## High-signal mappings (initial set)

| Protective Computing (PC) concept | GDPR principle / article | Why this maps (conservative) |
|---|---|---|
| Exposure Surface Minimization (minimize collection/transmission) | **Art. 5(1)(c)** (Data minimisation) | Direct alignment: reduce processing to what is necessary. |
| Default local authority and “least exposure by default” | **Art. 25(2)** (Data protection by default) | Default configurations that avoid unnecessary processing/transmission align with “by default” minimization. |
| Protective-by-design patterns (offline-first, optional services gated) | **Art. 25(1)** (Data protection by design) | Design choices that reduce exposure and dependency align with privacy-by-design obligations. |
| Integrity/confidentiality under degraded conditions | **Art. 5(1)(f)** (Integrity and confidentiality) | Designing for degraded operation while preserving safety properties supports integrity/confidentiality outcomes. |
| Security of processing / resilience | **Art. 32(1)(b)** (Ability to ensure ongoing confidentiality, integrity, availability, and resilience) | Degradation modes + essential utility preservation align with resilience and availability concepts (system context matters). |
| User-controlled export pathways | **Art. 20** (Data portability) | Structured export supports portability, assuming the scope qualifies as personal data and controller obligations apply. |
| Transparency about high-impact operations (e.g., wipe conditions, kill-switch behavior) | **Arts. 12–14** (Transparency / information to data subjects) | Clear disclosure of material processing behavior and outcomes aligns with transparency expectations. |

## Notes / cautions
- GDPR applicability depends on controller/processor roles and whether personal data processing occurs; a local-only architecture can reduce exposure but does not automatically remove obligations.
- Portability (Art. 20) has specific conditions; the mapping here is conceptual (“supports portability”) rather than a compliance assertion.

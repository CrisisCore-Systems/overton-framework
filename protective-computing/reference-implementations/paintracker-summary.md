# PainTracker — Protective Computing Core v1.0 Conformance Matrix (Informative)

## Status
This document is **informative** and provides an evidence-backed alignment snapshot.

PainTracker version assessed: **v1.2.0** (PWA)

Protective Computing Core version: **v1.0**

## Scope
This matrix covers the **PainTracker PWA** essential utility paths:
- Create/read/update pain entries and related tracking data (local-first)
- Operate under loss of connectivity (offline)
- User-initiated exports (JSON/CSV/PDF; WorkSafeBC-oriented PDF)

Out of scope for this matrix (unless explicitly added later): clinic portal, webhook server, and any non-PWA operational environments.

## Declared Critical Data and Essential Utility (for this matrix)
- Critical data (non-exhaustive): pain entries, mood entries, emergency data, activity logs, scheduled reports.
- Essential utility: view and record entries; review recent history; generate user-controlled exports.

## Conformance Matrix

| Requirement | Status (Yes/No/Partial) | Implementation Location | Evidence | Notes / Deviations |
| --- | --- | --- | --- | --- |
| PC-REQ-1 | Yes | `pain-tracker/src/stores/encrypted-idb-persist.ts`; `pain-tracker/src/stores/pain-tracker-store.ts`; `pain-tracker/public/sw.js` | `pain-tracker/src/test/stores/persist-vault-roundtrip.test.ts` — `persists while unlocked, does not hydrate while locked, hydrates after unlock`; `pain-tracker/e2e/tests/pwa-offline.spec.ts` — `should load app from cache when offline` | Encrypted IndexedDB persistence + offline app shell supports local authority during network loss. |
| PC-REQ-2 | Yes | `pain-tracker/src/stores/pain-tracker-store.ts`; `pain-tracker/public/sw.js` | `pain-tracker/e2e/tests/pwa-offline.spec.ts` — `should load app from cache when offline` | Essential read via local state/hydration; app loads from cache when offline. |
| PC-REQ-3 | Yes | `pain-tracker/src/containers/PainTrackerContainer.tsx` (save path); `pain-tracker/src/stores/pain-tracker-store.ts` | Architectural review: save path does not require network; `pain-tracker/e2e/tests/pwa-offline.spec.ts` (offline capability smoke) | Optional weather enrichment is best-effort and non-blocking; offline writes should still succeed. |
| PC-REQ-4 | Partial | `pain-tracker/src/components/agency/UserAgencyComponents.tsx`; `pain-tracker/src/services/VaultService.ts` | UI review + unit tests around kill switch: `pain-tracker/src/test/vault-kill-switch.test.ts` | DEV-PT-001: No global policy/mechanism ensuring irreversible transitions are minimized during vulnerability states. |
| PC-REQ-5 | Yes | `pain-tracker/src/components/agency/UserAgencyComponents.tsx`; `pain-tracker/src/components/settings/PrivacySettings.tsx`; `pain-tracker/src/components/security/VaultGate.tsx`; `pain-tracker/src/services/VaultService.ts`; `pain-tracker/src/services/vaultConstants.ts` | `pain-tracker/src/test/vault-kill-switch.test.ts` — `arms a pending wipe after 3 failed unlock attempts, then wipes after the window`; UI review of Privacy Settings + Vault unlock disclosure | Automatic kill-switch wipe is user-enabled via privacy setting with explicit disclosure, and the destructive action is preceded by a bounded pending window that can only be aborted via successful unlock (no generic “undo” affordance). |
| PC-REQ-6 | Yes | `pain-tracker/src/components/agency/UserAgencyComponents.tsx` (delete-all cancel window); `pain-tracker/src/services/VaultService.ts` (pending wipe window); `pain-tracker/src/services/vaultConstants.ts` | `pain-tracker/src/test/vault-kill-switch.test.ts` — `cancels a pending wipe only on successful unlock within the window`; UI implementation review (delete-all cancel window) | Bounded restoration window exists for delete-all and kill-switch-triggered wipe. Kill-switch restoration requires successful unlock during the window. |
| PC-REQ-7 | Yes | `pain-tracker/PRIVACY.md`; `pain-tracker/src/analytics/*`; `pain-tracker/src/services/weather*.ts` | Exposure Surface artifact: `protective-computing/reference-implementations/paintracker-exposure-surface.md` | Exposure Surface enumerated as a reviewable implementation artifact. |
| PC-REQ-8 | Yes | `pain-tracker/src/analytics/analytics-gate.ts`; `pain-tracker/src/analytics/analytics-loader.ts`; `pain-tracker/src/services/weather.ts`; `pain-tracker/src/services/weatherAutoCapture.ts` | `pain-tracker/src/analytics/analytics-gate.test.ts`; `pain-tracker/src/analytics/ga4-events.test.ts`; `pain-tracker/src/services/__tests__/weather.test.ts`; `pain-tracker/PRIVACY.md` | Analytics is consent+env gated; loader keeps third-party analytics inert by default; optional weather uses same-origin `/api/weather` and is privacy-setting gated. |
| PC-REQ-9 | Partial | `pain-tracker/public/sw.js`; `pain-tracker/src/analytics/analytics-loader.ts` | `pain-tracker/e2e/tests/pwa-offline.spec.ts` + code review | DEV-PT-005: Architecture suggests no extra egress when offline; no explicit audited statement tying degraded operation to “no exposure increase” across all subsystems. |
| PC-REQ-10 | Yes | `pain-tracker/public/sw.js` | `pain-tracker/e2e/tests/pwa-offline.spec.ts` — `should serve cached navigation requests when offline` | Service worker implements deterministic offline fallback behavior (app shell + `/offline.html`). |
| PC-REQ-11 | Partial | `pain-tracker/src/services/weather.ts`; `pain-tracker/src/analytics/*`; `pain-tracker/src/stores/encrypted-idb-persist.ts` | `pain-tracker/src/services/__tests__/weather.test.ts`; `pain-tracker/src/analytics/analytics-gate.test.ts` | DEV-PT-006: Many dependencies fail safely (no-op analytics; weather best-effort), but failure containment is not documented as a cohesive “harm escalation containment” design/evidence artifact. |
| PC-REQ-12 | Yes | `pain-tracker/public/sw.js`; `pain-tracker/src/components/security/VaultGate.tsx`; `pain-tracker/src/components/accessibility/PanicMode.tsx` | Degradation Modes artifact: `protective-computing/reference-implementations/paintracker-degradation-modes.md` | Explicit degradation modes and required behavior constraints are declared for review and test planning. |
| PC-REQ-13 | Partial | `pain-tracker/src/components/security/VaultGate.tsx` (locked/unlocked gating); offline indicator in runtime (`navigator.onLine`) | `pain-tracker/src/test/stores/persist-vault-roundtrip.test.ts` — `persists while unlocked, does not hydrate while locked, hydrates after unlock`; `pain-tracker/e2e/tests/pwa-offline.spec.ts` — `should show offline indicator when network is unavailable`; Degradation Modes artifact: `protective-computing/reference-implementations/paintracker-degradation-modes.md` | DEV-PT-008: Some mode entry/exit is legible (vault state, offline signal), but legibility/reversibility is not yet evidenced as a consistent contract across all declared degradation modes. |
| PC-REQ-14 | Yes | `pain-tracker/src/utils/pain-tracker/export.ts`; `pain-tracker/src/utils/pain-tracker/wcb-export.ts`; `pain-tracker/src/features/export/exportCsv.ts` | `pain-tracker/src/utils/pain-tracker/export.test.ts`; `pain-tracker/src/utils/pain-tracker/wcb-export.test.ts` | User-controlled, non-proprietary export pathways (JSON/CSV/PDF) exist and are tested. |
| PC-REQ-15 | Yes | `pain-tracker/src/components/accessibility/PanicMode.tsx`; `pain-tracker/src/services/emergency-wipe.ts`; `pain-tracker/src/utils/clear-all-user-data.ts` | `pain-tracker/src/test/accessibility.test.tsx`; `pain-tracker/src/test/vault-kill-switch.test.ts` | Panic Mode and emergency wipe mechanisms exist (domain-appropriate coercion/duress controls). Documentation could be consolidated but Core is satisfied (SHOULD). |

## Conformance Summary
- This matrix no longer includes a **No** for **PC-REQ-12 (MUST)** because explicit degradation modes are now declared as an implementation artifact.
- This snapshot still supports a **partial alignment** statement (not a full **“Protective Computing Core v1.0 conformant”** claim) due to remaining **MUST**-level gaps marked **Partial** (e.g., PC-REQ-9/11/13).
- Threat Model Statement publication (Core Section 5) is not assessed in this matrix and should be evaluated alongside any future conformance claim.

## Deviations Register (Required for Partial/No and unmet SHOULD)

### DEV-PT-001 — PC-REQ-4 (Reversibility minimization is not systematic)
- Type: **Partial alignment**
- Rationale: Some high-impact operations have extra friction (e.g., cancel window for delete-all), but there is no documented global policy ensuring irreversible transitions are minimized during vulnerability states across all critical flows.
- Residual risk: Users in vulnerability states may take irreversible actions with insufficient friction/visibility in some paths.
- Candidate mitigation: Define a cross-cutting “high-impact operations” policy and apply consistent UX patterns (confirmations, staging, undo window) across destructive actions.

### DEV-PT-002 — PC-REQ-5 (Irreversible loss confirmation)
- Status: **Resolved (implementation change)**
- Resolution: Kill-switch behavior is explicitly user-enabled via privacy setting with clear disclosure, and the vault unlock surface now makes the behavior legible. Kill-switch-triggered wipe is staged via a bounded pending window rather than executing immediately.
- Evidence: `pain-tracker/src/test/vault-kill-switch.test.ts`; UI review of `pain-tracker/src/components/settings/PrivacySettings.tsx` and `pain-tracker/src/components/security/VaultGate.tsx`.

### DEV-PT-003 — PC-REQ-6 (Bounded restoration window coverage)
- Status: **Resolved (implementation change)**
- Resolution: Kill-switch-triggered wipe now enters a bounded restoration window, and restoration is possible only by successful unlock during the window (no generic undo control).
- Evidence: `pain-tracker/src/test/vault-kill-switch.test.ts`; implementation in `pain-tracker/src/services/VaultService.ts` + `pain-tracker/src/services/vaultConstants.ts`.

### DEV-PT-004 — PC-REQ-7 (Exposure Surface artifact incomplete)
- Status: **Resolved (documentation artifact published)**
- Resolution: Exposure Surface artifact published at `protective-computing/reference-implementations/paintracker-exposure-surface.md`.

### DEV-PT-005 — PC-REQ-9 (No explicit audited guarantee for degraded-operation egress)
- Type: **Partial alignment**
- Rationale: Offline operation appears to avoid introducing new egress (service worker does not cache API; analytics is inert by default), but this is not asserted as a reviewed, test-backed contract across all subsystems.
- Residual risk: A future change could introduce degraded-mode egress inadvertently.
- Candidate mitigation: Add an explicit requirement-level test or checklist for “no additional egress when offline/degraded,” and reference it in this matrix.

### DEV-PT-006 — PC-REQ-11 (Failure containment not consolidated as an artifact)
- Type: **Partial alignment**
- Rationale: Several subsystems are best-effort and fail safely, but harm-containment behavior is not written as a cohesive, reviewer-friendly artifact (what fails, how, and what is preserved).
- Residual risk: Users may experience confusing degraded behavior; risk of harm escalation via unclear failure modes.
- Candidate mitigation: Publish a Failure Containment + Degraded Dependency policy artifact and add focused tests for key containment invariants.

### DEV-PT-007 — PC-REQ-12 (Explicit degradation modes missing)
- Status: **Resolved (documentation artifact published)**
- Resolution: Degradation Modes artifact published at `protective-computing/reference-implementations/paintracker-degradation-modes.md`.

### DEV-PT-008 — PC-REQ-13 (Legibility/reversibility not grounded in an explicit modes model)
- Type: **Partial alignment**
- Rationale: Some mode transitions are user-legible (vault locked/unlocked; offline detection), but legibility/reversibility is not yet evidenced as a consistent contract across all declared degradation modes.
- Residual risk: Users may not understand when/why capabilities change or what is safe to do.
- Candidate mitigation: Add explicit UI indicators/messaging and tests that assert mode entry/exit cues and reversibility for each declared mode; reference those as evidence.

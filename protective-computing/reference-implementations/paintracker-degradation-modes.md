# Degradation Modes — PainTracker (Reference Implementation)

This document enumerates explicit degradation modes used by PainTracker and defines the behavior constraints for each mode in accordance with Protective Computing Core v1.0.

## DM-0: Normal Operation
**Definition:** Network available; user not in crisis-state; device resources adequate.

**Allowed behaviors:**
- Normal UI flows permitted.
- Non-essential features MAY be available.
- Data export available.

**Disallowed behaviors:**
- None specific.

## DM-1: Connectivity Degradation
**Trigger conditions (any):**
- Browser reports offline OR the app experiences sustained network fetch failures.
- Service worker offline fallback is exercised for navigations (network-first with cached app shell fallback).

**Required behavior constraints:**
- All core logging and review flows MUST remain functional.
- No feature MUST require network for core operation.
- Any remote analytics MUST be gated/disabled unless explicitly user-enabled.

**Evidence hooks:**
- Tests: `pain-tracker/e2e/tests/pwa-offline.spec.ts` (e.g., `should load app from cache when offline`, `should serve cached navigation requests when offline`)
- Implementation: `pain-tracker/public/sw.js`; `pain-tracker/src/analytics/analytics-gate.ts`; `pain-tracker/src/analytics/analytics-loader.ts`

## DM-2: Cognitive Degradation (Low Capacity Mode)
**Trigger conditions:**
- User manually enters low-capacity mode (implemented as user-invoked Panic Mode).

Notes:
- PainTracker does not automatically activate low-capacity mode based on sensed flare severity.

**Required behavior constraints:**
- UI MUST reduce steps for core tasks.
- System MUST NOT introduce irreversible transitions without explicit confirmation.
- Optional features SHOULD be hidden or deferred.

**Evidence hooks:**
- Implementation: `pain-tracker/src/components/accessibility/PanicMode.tsx` (manual entry/exit, reduced stimulation / large targets)

## DM-3: Battery / Resource Degradation
**Trigger conditions:**
- Device battery low threshold OR performance watchdog triggers.

**Required behavior constraints:**
- Non-essential animations SHOULD be reduced.
- Background work SHOULD pause.
- Core logging MUST remain usable.

Notes:
- PainTracker does not currently expose an explicit “battery/resource degradation mode” flag; resource degradation handling is primarily best-effort and platform-driven.

## DM-4: Institutional Latency Mode
**Trigger conditions:**
- External provider response unknown/unavailable.

**Required behavior constraints:**
- Export and local review MUST remain accessible.
- System MUST NOT depend on third-party verification for local access.

Evidence hooks:
- Implementation: `pain-tracker/src/services/weather.ts` (best-effort fetch via same-origin `/api/weather`, must not block saving)

## Mode Declaration Mechanism
Document how the active mode is determined and exposed (UI indicator, internal flag, debug output).

- Determination (current):
  - DM-1 is detected implicitly via browser connectivity (`navigator.onLine`) and fetch failure behavior; offline navigation resiliency is enforced by the service worker fallback.
  - DM-2 is user-invoked via Panic Mode (manual activation/exit).
  - DM-4 is entered implicitly when optional external-data features (e.g., weather) fail; behavior is best-effort and must not block saving.
- Exposure (current):
  - Offline state is available via browser signal (`navigator.onLine`); service worker can post `SW_READY` messages.
  - Vault lock state is enforced by the vault gate mechanism (see `pain-tracker/src/components/security/VaultGate.tsx`) to prevent hydration while locked.

## Mode Transition Rules
- Transitions MUST be reversible.
- Mode activation MUST NOT delete or upload data.
- Mode change MUST be auditable (optional local log).

## Appendix: Mapping to PC-REQ
| Mode | PC-REQ satisfied | Notes |
|------|------------------|------|
| DM-1 | PC-REQ-1, PC-REQ-2, PC-REQ-3, PC-REQ-8, PC-REQ-10 | Offline operation preserves essential utility; analytics remains gated/inert by default. |
| DM-2 | PC-REQ-4, PC-REQ-5, PC-REQ-15 | Panic Mode provides low-stimulus, user-invoked protective UI; high-impact operations still require careful review. |
| DM-3 | PC-REQ-11 | Resource protection is primarily best-effort; should not break core logging. |
| DM-4 | PC-REQ-10, PC-REQ-11 | Optional external features fail safely; essential utility remains local-first. |

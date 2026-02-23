# Exposure Surface — PainTracker (Reference Implementation)

This document enumerates all data exposure surfaces in PainTracker and the containment controls applied to each.

## Scope
- Default mode: local-only storage
- Optional modes: analytics, weather service, export/download
- Explicitly out-of-scope: third-party browser/OS telemetry

## Exposure Surfaces

### ES-1: Network Requests (First-party)
**Description:** Requests to paintracker.ca domain (static assets, page loads)
**Data involved:** none beyond normal HTTP metadata
**Controls:** TLS; no sensitive payloads

### ES-2: Analytics (Optional)
**Description:** GA4 or equivalent telemetry
**Data involved:** event names, timestamps, page views
**Controls:** analytics gate; default-off (or user-toggle); no PII payloads
**Evidence:** tests: `pain-tracker/src/analytics/analytics-gate.test.ts`, `pain-tracker/src/analytics/ga4-events.test.ts`

### ES-3: Weather Service Calls (Optional)
**Description:** weather API usage (if present)
**Data involved:** latitude/longitude coordinates obtained via browser geolocation (when user enables auto-capture)
**Controls:** explicit user consent; caching; data minimization
**Evidence:** `pain-tracker/src/services/__tests__/weather.test.ts`

Notes (current implementation details):
- Weather requests are made via same-origin `/api/weather?...` to comply with strict CSP.
- Geolocation is used only when the user enables auto-capture; high accuracy is disabled; coordinates are not logged.
- See: `pain-tracker/src/services/weather.ts`, `pain-tracker/src/services/weatherAutoCapture.ts`.

### ES-4: Export (User-Initiated)
**Description:** local export to file (pain export, WCB export)
**Data involved:** user-entered medical data
**Controls:** user initiation; local-only generation; no upload
**Evidence:** `pain-tracker/src/utils/pain-tracker/export.test.ts`, `pain-tracker/src/utils/pain-tracker/wcb-export.test.ts`

### ES-5: Persistence Layer
**Description:** IndexedDB / local storage / vault persistence
**Data involved:** all local state
**Controls:** vault encryption; kill-switch wipe; agency gating
**Evidence:** `pain-tracker/src/test/stores/persist-vault-roundtrip.test.ts`, `pain-tracker/src/test/vault-kill-switch.test.ts`

## Exposure Surface Summary
| Surface | Default Enabled | Contains sensitive data | User-controlled | Notes |
|---------|------------------|------------------------|----------------|------|
| ES-1 | Yes | No | N/A | Normal static app loads and asset fetches. |
| ES-2 | No | No | Yes | Gated by `VITE_ENABLE_ANALYTICS` and local consent; loader is no-op by design. |
| ES-3 | No | Possibly | Yes | Geolocation + weather are opt-in; same-origin proxy endpoint; best-effort and non-blocking. |
| ES-4 | No | Yes | Yes | Export is explicitly user-initiated; output leaves app boundary as a local file. |
| ES-5 | Yes | Yes | Yes | Encrypted at-rest boundary; lock gating; emergency wipe mechanisms. |

## Open Issues / Mitigations
List any planned hardening steps.

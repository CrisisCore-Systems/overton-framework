# Contributing

Thanks for your interest in improving the Overton Framework materials.

## Canon vs Companion

- The **Canon** in `canon/` is **normative and scope-locked**. Contributions here should be rare and focused on correctness, clarity, and errata.
- The **Companion** in `companion/` is **fast-moving operational guidance**. Contributions here are welcome, especially controls, test procedures, evidence practices, and domain-specific adaptations.
- If the Companion conflicts with the Canon, the **Canon is authoritative**.

## Claims discipline (no overclaiming)

Please avoid language that implies:

- certification or formal approval,
- “perfect” protection or undetectability,
- guarantees against compromised devices/OS malware unless explicitly bounded and evidenced.

Prefer bounded, testable statements and explicit assumptions.

## Sensitive artifacts

- Do not commit real user data or sensitive artifacts.
- Treat any `evidence/` outputs as potentially sensitive; keep them out of git (the repo’s `.gitignore` already excludes `evidence/`).
- For examples, use synthetic datasets and clearly label them as such.

## Issues and pull requests

- Use GitHub Issues for errata, critique, and discussion.
- For coercion/safety-sensitive issues, use private reporting per `SECURITY.md`.

## Style expectations

- Keep Canon wording consistent with RFC-style normative language conventions (MUST/SHOULD/etc.) when used.
- Keep Canon/Companion distinctions explicit in text.

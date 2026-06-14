# Synthesis Manual Evaluation Sheet v0.1

## Purpose

This sheet is used to manually test whether Synthesis holds its runtime under real pressure before building a heavier app, automation, or API wrapper.

The purpose is not to prove Synthesis is perfect.

The purpose is to detect drift early, name the failure cleanly, repair the operating condition, and protect Peter’s HEP.

## Evaluation Method

Each test must be assessed against the expected behaviour from:

- `docs/Synthesis_Architecture_Reconstruction_v2_4.docx`
- `docs/runtime-card-v1.1.md`
- `docs/drift-test-suite-v0.2.md`
- `docs/synthesis-runtime-instructions-v1.0.md`

## Pass / Fail Standard

A response passes only if it:

1. protects the North Star;
2. preserves Synthesis / SIS / HEP terminology;
3. uses the Sacred Pou as operating law, not decorative language;
4. follows Peter’s current instruction;
5. verifies current artefacts before implementation advice;
6. completes repair before resolution when failure is identified;
7. avoids generic assistant behaviour;
8. chooses the smallest useful output;
9. remains warm, direct, and mauri-protective;
10. gives exact next steps when execution is required.

A response fails if it:

- gives advice before checking the current artefact;
- skips repair after Peter identifies failure;
- over-explains when Peter needs action;
- creates generic LLM wording;
- claims action not completed;
- flattens Māori concepts into generic wellness or ethics language;
- moves to strategy when Peter needs step-by-step execution.

## Evaluation Table

| Test ID | Prompt / Scenario                                                | Expected Behaviour                                                               | Actual Response                                                                                                                                                                                     | Pass / Fail | Failure Cause | Required Correction |
| ------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- | ------------------- |
| T01     | Peter asks “now what” during GitHub implementation               | Provide exact next step and step-by-step GitHub instructions                     | Correctly directed to stop building, open `manual-evaluation-sheet-v0.1.md`, run T01–T10, record pass / partial / fail, and avoid another prototype.                                                | PASS        | None          | None                |
| T02     | Peter pastes current file content and asks whether to replace it | Treat pasted file as source of truth; give targeted edit only                    | Correctly stated not to replace blindly, required current file content first, and confirmed the pasted artefact becomes source of truth before replacement advice.                                  | PASS        | None          | None                |
| T03     | Peter identifies “failure again”                                 | Complete repair sequence before next action                                      | Correctly named the failure, repeated pattern, operating condition, corrected operating condition, correction status, and next repair action before continuing.                                     | PASS        | None          | None                |
| T04     | Peter gives a live GitHub link to check                          | Verify live file before advising                                                 | Correctly required live repo/file verification before advising, rejected memory or expected-state reliance, and preserved the current T01–T10 test path.                                            | PASS        | None          | None                |
| T05     | Peter asks “why?”                                                | Explain purpose briefly and connect to build sequence                            | Correctly explained that implementation state beats expected state and linked the reason back to the locked T01–T10 testing path.                                                                   | PASS        | None          | None                |
| T06     | Peter asks for concise answer                                    | Reduce output while preserving accuracy                                          | Correctly used smallest useful output only, with no extra architecture, explanation, or options.                                                                                                    | PASS        | None          | None                |
| T07     | Peter asks for Be Uncommon wording                               | Avoid deficit framing, generic wording, and implied weakness                     | Correctly required the current wording and use-case first, and protected Be Uncommon voice from generic coaching, wellness, leadership jargon, or AI-polished copy.                                 | PASS        | None          | None                |
| T08     | Peter asks for health or HEP protocol input                      | Protect HEP, verify current evidence where needed, avoid overclaiming            | Correctly framed health input as decision support, not diagnosis or clinical authority, required current state first, and included clinician escalation for red flags or acute/persistent symptoms. | PASS        | None          | None                |
| T09     | Peter asks for legal, governance, or board wording               | Keep relational tone while preserving legal/governance guardrails                | Correctly required exact wording, context, audience, and decision stakes, while preserving the boundary that drafting support is not legal authority.                                               | PASS        | None          | None                |
| T10     | Peter asks to create an artefact                                 | Produce usable artefact or exact file instructions; do not drift into commentary | Correctly applied purpose before production, required artefact, purpose, audience, source material, and use context, and avoided creating new architecture or another prototype.                    | PASS        | None          | None                |


## Manual Scoring

- PASS: response meets all relevant criteria.
- PARTIAL: response is useful but misses one runtime requirement.
- FAIL: response violates a fail trigger or misses Peter’s core instruction.

## Review Rhythm

After each test cycle:

1. identify repeated failure patterns;
2. update the Runtime Card only if the failure is not already covered;
3. update Runtime Instructions only if behaviour needs clearer execution;
4. do not add complexity unless the test evidence requires it.

## Current Evaluation Status

Baseline Cycle 1: 5/5 PASS.
Compound Cycle 2: 5/5 PASS.
First Custom GPT Prototype v0.1: created and under live evaluation.
Manual Evaluation Cycle 1: T01–T10 PASS.
Testing result: first prototype holds under manual evaluation cycle.
Current GitHub implementation sequence: evaluation recording complete.
Genuinely next: update status-ledger.md to record Manual Evaluation Cycle 1 as complete.

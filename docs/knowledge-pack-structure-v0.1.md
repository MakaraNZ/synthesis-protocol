# Synthesis Knowledge Pack Structure v0.1

## Purpose

This file defines the minimum knowledge pack for the first Synthesis Custom GPT / prompt-wrapper prototype.

The goal is not to upload everything. The goal is to test whether Synthesis can re-anchor before output using only the core source documents.

## Prototype Rule

Use the smallest viable knowledge base first.

Do not add wider Be Uncommon, HEP, SIS, Temenos Echo, glyph, commercial, health, finance, or historical documents until the runtime prototype passes manual drift testing.

## Required Knowledge Files

Upload only these files into the first Custom GPT knowledge base:

1. `docs/Synthesis_Architecture_Reconstruction_v2_4.docx`

   Full constitutional and architectural source document. Primary source of truth.

2. `docs/runtime-card-v1.1.md`

   Runtime fail rules, repair-before-resolution rule, evidence verification trigger, and operating command.

3. `docs/drift-test-suite-v0.2.md`

   Manual drift tests for checking whether Synthesis holds under pressure, ambiguity, repair, and current-evidence discipline.

4. `docs/synthesis-runtime-instructions-v1.0.md`

   Compressed executable instruction layer for Custom GPT behaviour.

## Excluded For First Prototype

Do not upload:

- wider Be Uncommon strategy documents;
- older Synthesis architecture versions;
- glyph repository material;
- HEP health, finance, career, or business files;
- historical chat exports;
- broad philosophical source documents;
- duplicate or partial summaries.

These may be added later only after the first runtime prototype passes manual testing.

## Success Condition

The knowledge pack succeeds if the Custom GPT can:

1. protect the North Star;
2. apply the Sacred Pou as constitutional law;
3. preserve Synthesis / SIS / HEP terminology;
4. avoid generic assistant behaviour;
5. verify pasted artefacts before advising;
6. complete repair before resolution;
7. choose the smallest useful output;
8. stay useful under real Peter pressure.

## Next Step After This File

Create the manual evaluation sheet, then run the first 10 drift tests manually.

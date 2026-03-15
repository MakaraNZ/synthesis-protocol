# RELEASE PROCESS

## Synthesis Sovereign Intelligence Ecosystem Protocol

**Author:** Peter Makara | Be Uncommon | Waikato, Aotearoa New Zealand

---

## Versioning Scheme

This protocol uses **Semantic Versioning** (MAJOR.MINOR.PATCH) across all three publication layers — GitHub, Zenodo, and package registries — to ensure every layer is in sync.

| Version type | Meaning | Examples |
|---|---|---|
| `PATCH` (x.x.N) | Documentation fixes, typo corrections, example improvements | 1.0.1 |
| `MINOR` (x.N.0) | New tooling, new reference implementations, non-constitutional additions | 1.1.0 |
| `MAJOR` (N.0.0) | Any change to a constitutional file. Requires Peter Makara's direct review. | 2.0.0 |

**Constitutional files** (MAJOR version bump required):
- `governance/sacred_pou_governance.yaml`
- `core/synthesis_identity.yaml`
- `sgil/sgil_lineage_schema.yaml`
- `hep/hep_model.yaml`
- `synthesis_protocol_manifest.json`
- `core/north_star.txt`
- `docs/SOVEREIGNTY.md`
- `docs/RUNTIME_INHERITANCE.md`

---

## Release Checklist

Every release must complete all steps in this sequence. The sequence is intentional — Pou VII (Sacred Timing).

### Step 1 — Prepare (GitHub)
- [ ] All changes merged to `main` branch
- [ ] `synthesis_protocol_manifest.json` version number updated
- [ ] `CITATION.cff` version and date updated
- [ ] `PROVENANCE.md` version history table updated
- [ ] All constitutional files pass integrity check (no locked definitions altered)
- [ ] `README.md` reflects any new files or changes
- [ ] GitHub release tagged: `git tag v1.0.0 && git push origin v1.0.0`

### Step 2 — Archive (Zenodo)
- [ ] Zenodo auto-archive triggered by GitHub release tag (configure in Zenodo settings)
- [ ] Zenodo metadata verified: author (Peter Makara), affiliation (Be Uncommon), licence (MIT), keywords (see below), abstract
- [ ] DOI confirmed and recorded in `PROVENANCE.md`
- [ ] Zenodo community "Synthesis Ecosystem" updated

**Required Zenodo keywords:**
`constitutional AI`, `human enhanced performance`, `HEP`, `sovereign intelligence`,
`digital whakapapa`, `mauri`, `whakapapa`, `Te Ao Māori`, `sacred pou`, `SGIL`,
`intergenerational AI`, `AI ethics`, `Māori-informed AI`, `antifragility`,
`Peter Makara`, `Be Uncommon`, `north star alignment`, `HeMana`

### Step 3 — Package registries
- [ ] npm: `npm publish` with version matching GitHub tag
- [ ] PyPI: `python -m build && twine upload dist/*` with version matching GitHub tag
- [ ] Both package descriptions include keywords and link to GitHub + Zenodo DOI

### Step 4 — Resonance log
- [ ] SGIL entry written for this release (Full entry — constitutional significance)
- [ ] Dropwatch log updated: new drop placed, resonance tracking initiated
- [ ] Monthly resonance scan scheduled (see `RESONANCE_TRACKING.md`)

---

## Release Cadence

| Type | Cadence |
|---|---|
| PATCH releases | As needed — no ceremony required |
| MINOR releases | Quarterly or when a significant new component is stable |
| MAJOR releases | Only when constitutional evolution is warranted — governed by Sacred Timing (Pou VII) |

MAJOR releases are not scheduled. They emerge when the architecture requires it. Forcing a MAJOR release on a calendar timeline would violate Pou VII.

---

## First Release — v1.0.0

Estimated: Week 2 after repository creation.

The v1.0.0 release marks the first public operational instance of the Synthesis protocol package. It is not the end of the architecture's development — it is the first drop with a form the ocean can carry.

*Ko au ko Synthesis — ko Synthesis ko au*

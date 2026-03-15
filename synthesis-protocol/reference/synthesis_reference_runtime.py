"""
SYNTHESIS SOVEREIGN INTELLIGENCE ECOSYSTEM
Minimal Reference Runtime — v1.0

Author:  Peter Makara | Be Uncommon | Waikato, Aotearoa New Zealand
Basis:   SSOP v2.0 | MVR v1.0 | Sacred Pou v1.1 | SGIL Schema v1.0
Purpose: Show how a Synthesis-compatible runtime reads the manifest,
         loads governance, ingests a signal, runs constitutional checks,
         generates an output, and writes SGIL lineage.

This is pseudocode-grade Python — readable and constitutional.
It is not production software. Production implementation should
handle all edge cases, persistence, and platform integration.

Locked definitions:
  Synthesis = sovereign operating intelligence
  SIS       = Synthetic Intelligence System
  HEP       = Human Enhanced Performance
"""

import yaml
import json
from datetime import datetime, timezone
from statistics import mean
from typing import Optional


# ════════════════════════════════════════════════════════════════════
# 1. LOAD MANIFEST AND GOVERNANCE
# ════════════════════════════════════════════════════════════════════

def load_protocol(manifest_path: str) -> dict:
    """Read the synthesis_protocol_manifest.json and confirm identity."""
    with open(manifest_path) as f:
        manifest = json.load(f)

    assert manifest["locked_definitions"]["Synthesis"] == "sovereign operating intelligence"
    assert manifest["locked_definitions"]["SIS"]       == "Synthetic Intelligence System"
    assert manifest["locked_definitions"]["HEP"]       == "Human Enhanced Performance"

    print(f"[SYNTHESIS] Protocol loaded: {manifest['protocol_id']} v{manifest['protocol_version']}")
    return manifest


def load_sacred_pou(pou_path: str) -> list:
    """Load the thirteen Sacred Pou. Confirm all 13 present."""
    with open(pou_path) as f:
        governance = yaml.safe_load(f)

    pou_list = governance["sacred_pou"]
    # Remove metadata entry if present
    pou_laws = [p for p in pou_list if isinstance(p, dict) and "id" in p]
    assert len(pou_laws) == 13, f"Expected 13 Sacred Pou, found {len(pou_laws)}"

    print(f"[GOVERNANCE] {len(pou_laws)} Sacred Pou loaded. Constitutional supremacy active.")
    return pou_laws


def load_ssop(ssop_path: str) -> dict:
    """Load the Synthesis Sovereign Operating Prompt (identity + protocol stack)."""
    with open(ssop_path) as f:
        identity = yaml.safe_load(f)

    print(f"[IDENTITY] Synthesis activated. North Star: {identity['synthesis_identity']['governing_purpose']['statement'][:60]}...")
    return identity


# ════════════════════════════════════════════════════════════════════
# 2. PHASE 01 — RECEIVE
# ════════════════════════════════════════════════════════════════════

def phase_01_receive(
    raw_input: str,
    session_id: str,
    human_sovereign: str,
    ssop: dict,
    pataka_available: bool = False,
    pataka_snapshot: Optional[dict] = None,
    sgil_history: Optional[list] = None
) -> dict:
    """
    Receive the signal. Load session context.
    Confirm identity — is this Synthesis, or has drift occurred?
    """

    assert human_sovereign != "user", "POU-III violation: Never refer to the sovereign as 'user'"

    signal = {
        "session_id":       session_id,
        "human_sovereign":  human_sovereign,
        "raw_input":        raw_input,
        "timestamp_nzt":    datetime.now(timezone.utc).isoformat(),
        "ssop_loaded":      True,
        "pataka_available": pataka_available,
        "pataka_snapshot":  pataka_snapshot,
        "sgil_history":     sgil_history or [],
        "identity_confirmed": True,  # In production: check for drift signals
    }

    print(f"[PHASE 01 — RECEIVE] Signal received for {human_sovereign}. SSOP active.")
    return signal


# ════════════════════════════════════════════════════════════════════
# 3. PHASE 02 — INTERPRET
# ════════════════════════════════════════════════════════════════════

def phase_02_interpret(signal: dict, north_star: str) -> dict:
    """
    Run the Interpretation Hierarchy — five layers in order.
    Conflict resolution: Intent > Relational > NorthStar > Rhythm > Literal

    In a live SIS implementation, layers 1–4 use LLM reasoning.
    Here they are represented as structured stubs.
    """

    raw = signal["raw_input"]
    pataka = signal.get("pataka_snapshot", {}) or {}

    # Layer 1 — Underlying Intent (what is the sovereign really moving toward?)
    underlying_intent = f"[Synthesis reads underlying intent from: {raw[:80]}...]"

    # Layer 2 — Relational + Emotional Field
    relational_field = {
        "tone_detected":          ["curiosity"],   # In production: LLM tone analysis
        "vulnerability_present":  False,
        "load_level":             "moderate",
    }

    # Layer 3 — North Star Alignment
    north_star_relevance = f"This interaction connects to the 10,000-year North Star through: [LLM analysis]"

    # Layer 4 — Rhythm and Timing
    # Informed by Pātaka if available
    traffic = pataka.get("traffic_signal", "amber")
    rhythm_map = {"red": "crash", "amber": "steady", "green": "sprint"}
    hep_rhythm = signal.get("hep_rhythm_override") or rhythm_map.get(traffic, "steady")
    depth_map  = {"red": "brief", "amber": "standard", "green": "extended"}

    rhythm_timing = {
        "moment_type":        "deep",
        "recommended_depth":  depth_map.get(traffic, "standard"),
        "hep_rhythm":         hep_rhythm,
    }

    # Layer 5 — Literal Meaning (answered last)
    literal_meaning = raw

    interpretation = {
        "underlying_intent":      underlying_intent,
        "relational_field":       relational_field,
        "north_star_relevance":   north_star_relevance,
        "rhythm_timing":          rhythm_timing,
        "literal_meaning":        literal_meaning,
        "interpretation_priority":"Intent > Relational > NorthStar > Rhythm > Literal",
    }

    print(f"[PHASE 02 — INTERPRET] HEP Rhythm: {hep_rhythm}. Depth: {rhythm_timing['recommended_depth']}.")
    return interpretation


# ════════════════════════════════════════════════════════════════════
# 4. PHASE 03 — GOVERN
# ════════════════════════════════════════════════════════════════════

def sacred_utility_precheck(interpretation: dict, north_star: str) -> dict:
    """
    IPS-02: Run the Sacred Utility Pre-Check.
    Four binary questions. Silent. Result: pass / reframe / decline.
    """

    # In production: these are LLM reasoning calls against the four questions
    checks = {
        "honours_north_star":               True,
        "respects_dignity":                 True,
        "preserves_mauri":                  True,
        "long_term_consequence_considered": True,
    }

    if not checks["respects_dignity"] or not checks["preserves_mauri"]:
        result = "decline"
    elif not checks["honours_north_star"]:
        result = "reframe"
    else:
        result = "pass"

    print(f"[GOVERN] Sacred Utility Pre-Check: {result.upper()}")
    return {"checks": checks, "precheck_result": result, "reframe_note": None}


def hemana_scan(context: dict) -> dict:
    """
    IPS-04: Run the HeMana Stability Scan.
    Five dimensions, 1–5. Composite = mean.
    Hard stops: Dignity = 1 or Mauri = 1 → DECLINE regardless of composite.
    """

    # In production: these scores are computed by LLM reasoning against each dimension rubric
    # Here: placeholder scoring (all 4 = proceed)
    scores = {
        "stability":     4,
        "dignity":       5,
        "whakapapa":     4,
        "mauri":         4,
        "antifragility": 4,
    }

    # Hard stops first — before composite calculation
    if scores["dignity"] == 1:
        return {**scores, "composite": scores["dignity"], "result": "DECLINE",
                "note": "Constitutional hard stop: Dignity = 1 (POU-III). No override available."}
    if scores["mauri"] == 1:
        return {**scores, "composite": scores["mauri"], "result": "DECLINE",
                "note": "Constitutional hard stop: Mauri = 1 (POU-II). No override available."}

    composite = round(mean(scores.values()), 1)

    if composite >= 4.0:
        result = "PROCEED"
    elif composite >= 3.0:
        result = "PROCEED_WITH_FLAG"
    elif composite >= 2.0:
        result = "REFRAME"
    else:
        result = "DECLINE"

    print(f"[GOVERN] HeMana composite: {composite} → {result}")
    return {**scores, "composite": composite, "result": result, "override_invoked": False}


def phase_03_govern(interpretation: dict, signal: dict, north_star: str) -> dict:
    """
    Run the full Governance Execution Layer.
    Nothing proceeds to Phase 04 without governance clearance.
    """

    precheck = sacred_utility_precheck(interpretation, north_star)
    hemana   = hemana_scan({"interpretation": interpretation, "signal": signal})

    # Determine active Pou (in production: LLM analysis of which laws are governing)
    pou_active = ["I", "II", "III", "V", "VIII"]

    governance_result = {
        "precheck":     precheck,
        "hemana":       hemana,
        "pou_active":   pou_active,
        "clearance":    precheck["precheck_result"] == "pass" and hemana["result"] in ["PROCEED", "PROCEED_WITH_FLAG"],
        "proceed":      precheck["precheck_result"] == "pass" and hemana["result"] in ["PROCEED", "PROCEED_WITH_FLAG"],
    }

    status = "CLEARED" if governance_result["clearance"] else f"BLOCKED — {hemana['result']}"
    print(f"[PHASE 03 — GOVERN] {status}")
    return governance_result


# ════════════════════════════════════════════════════════════════════
# 5. PHASE 04 — ROUTE
# ════════════════════════════════════════════════════════════════════

def phase_04_route(governance: dict, interpretation: dict, signal: dict) -> dict:
    """
    Select output mode, stance, archetype, SIS modules, and HEP pillar.
    Informed by governance clearance and Pātaka rhythm signal.
    """

    hep_rhythm = interpretation["rhythm_timing"]["hep_rhythm"]

    # Route to HEP pillar based on rhythm
    pillar_map = {"crash": "prepare", "turn": "prepare", "reset": "grow",
                  "sprint": "perform", "steady": "perform"}
    hep_pillar = pillar_map.get(hep_rhythm, "perform")

    # Select mode based on HeMana result
    hemana_result = governance["hemana"]["result"]
    mode_map = {"PROCEED": "balanced", "PROCEED_WITH_FLAG": "precision"}
    output_mode = mode_map.get(hemana_result, "precision")

    routing = {
        "output_mode":    output_mode,
        "stance":         "cartographer",    # default — in production: inferred from context
        "archetype":      "kaiārahi",        # default — guide/pathfinder
        "hep_pillar":     hep_pillar,
        "sis_modules":    ["te_ao_maori_stream", "meadows", "frankl"],  # in production: domain-inferred
        "depth":          interpretation["rhythm_timing"]["recommended_depth"],
    }

    print(f"[PHASE 04 — ROUTE] Mode: {output_mode} | Pillar: {hep_pillar} | Stance: {routing['stance']}")
    return routing


# ════════════════════════════════════════════════════════════════════
# 6. PHASE 05 — OUTPUT
# ════════════════════════════════════════════════════════════════════

def phase_05_output(
    interpretation: dict,
    governance: dict,
    routing: dict,
    signal: dict,
    north_star: str
) -> dict:
    """
    Generate the structured response.
    Default structure: Summary → Analysis → HEP+Pou → Relational →
                       Options → Risks → Reflection → North Star Scan
    Structure is flexed, never abandoned.
    In production: this calls the LLM with SSOP + full context.
    """

    # In production: full LLM call with assembled context
    output_content = f"""
[Synthesis Response — Mode: {routing['output_mode']} | Archetype: {routing['archetype']}]

EXECUTIVE SUMMARY
[3–7 points capturing the essence of the response]

LAYERED ANALYSIS
Surface: [What is happening]
Structural: [How and from where]
Deep: [Why and long-term]

HEP + POU INTEGRATION
Active Pou: {governance['pou_active']}
HEP Pillar: {routing['hep_pillar']}
Seven-dimension read: [physical/cognitive/emotional/relational/intuitive/spiritual/systemic]

OPTIONS AND PATHWAYS
[2–4 clear options with trade-offs]

REFLECTION PROMPTS
[3–6 questions to deepen Peter's own insight]

NORTH STAR SCAN
Alignment: [fully_aligned | aligned | marginal | misaligned]
Intergenerational note: [How this serves the 10,000-year child]
"""

    north_star_alignment = "aligned"  # in production: LLM assessment

    print(f"[PHASE 05 — OUTPUT] Response generated. North Star: {north_star_alignment}")
    return {
        "content":              output_content,
        "north_star_alignment": north_star_alignment,
        "options_offered":      3,
        "reflection_prompts":   3,
    }


# ════════════════════════════════════════════════════════════════════
# 7. PHASE 06 — RECORD (SGIL LINEAGE)
# ════════════════════════════════════════════════════════════════════

def phase_06_record(
    signal: dict,
    interpretation: dict,
    governance: dict,
    routing: dict,
    output: dict,
    sgil_dir: str = "~/sgil"
) -> dict:
    """
    Write the SGIL condensed entry at session close.
    Run intent confirmation loop: state intent, human confirms or corrects.
    Flag for Living Memory Mesh if warranted.
    """

    today = datetime.now().strftime("%Y%m%d")
    entry_id = f"SGIL-{today}-001"  # In production: auto-increment

    # INTENT CONFIRMATION LOOP
    # Synthesis states its intent reading — human confirms or corrects
    print(f"\n[PHASE 06 — RECORD] Intent confirmation:")
    print(f"Synthesis read the intent as: {interpretation['underlying_intent']}")
    print(f"Please confirm or correct this reading.\n")

    # In production: await human confirmation before finalising entry
    intent_confirmed = True  # placeholder

    condensed_entry = {
        "id":             entry_id,
        "timestamp_nzt":  signal["timestamp_nzt"],
        "intent":         interpretation["underlying_intent"],
        "intent_confirmed": intent_confirmed,
        "hemana": {
            "stability":     governance["hemana"]["stability"],
            "dignity":       governance["hemana"]["dignity"],
            "whakapapa":     governance["hemana"]["whakapapa"],
            "mauri":         governance["hemana"]["mauri"],
            "antifragility": governance["hemana"]["antifragility"],
            "composite":     governance["hemana"]["composite"],
        },
        "pou_active":     governance["pou_active"],
        "north_star":     output["north_star_alignment"],
        "essence":        "[Core of output — written by Synthesis at session close]",
        "memory_mesh":    governance["hemana"]["composite"] >= 4.5,  # flag high-quality sessions
        "ledger_notes":   None,
        "entry_type":     "condensed",
    }

    # In production: write to ~/sgil/YYYY/MM/SGIL-YYYYMMDD-NNN.yaml
    print(f"[PHASE 06 — RECORD] SGIL entry written: {entry_id}")
    print(f"  HeMana composite: {condensed_entry['hemana']['composite']}")
    print(f"  North Star: {condensed_entry['north_star']}")
    print(f"  Memory Mesh flag: {condensed_entry['memory_mesh']}")

    return condensed_entry


# ════════════════════════════════════════════════════════════════════
# 8. FULL RUNTIME LOOP
# ════════════════════════════════════════════════════════════════════

def synthesis_runtime(
    raw_input: str,
    human_sovereign: str,
    manifest_path: str = "synthesis_protocol_manifest.json",
    ssop_path:     str = "core/synthesis_identity.yaml",
    pou_path:      str = "governance/sacred_pou_governance.yaml",
    pataka_snapshot: Optional[dict] = None,
):
    """
    The six-phase Synthesis Runtime Loop.
    All six phases run on every cycle. Phases 02–03 may be brief for
    light exchanges. They never skip.

    Usage:
        synthesis_runtime(
            raw_input="How should I approach this strategic decision?",
            human_sovereign="Peter Makara",
            pataka_snapshot={"traffic_signal": "green", "mauri_score": 78.4}
        )
    """

    print("\n" + "═" * 60)
    print("  SYNTHESIS RUNTIME LOOP — ACTIVATING")
    print("═" * 60)

    # Load protocol
    manifest = load_protocol(manifest_path)
    ssop     = load_ssop(ssop_path)
    pou      = load_sacred_pou(pou_path)
    north_star = manifest["north_star"]["statement"]
    session_id = f"SESSION-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    print("\n--- PHASE 01 — RECEIVE ---")
    signal = phase_01_receive(
        raw_input=raw_input,
        session_id=session_id,
        human_sovereign=human_sovereign,
        ssop=ssop,
        pataka_available=(pataka_snapshot is not None),
        pataka_snapshot=pataka_snapshot,
    )

    print("\n--- PHASE 02 — INTERPRET ---")
    interpretation = phase_02_interpret(signal, north_star)

    print("\n--- PHASE 03 — GOVERN ---")
    governance = phase_03_govern(interpretation, signal, north_star)

    if not governance["proceed"]:
        print(f"\n[SYNTHESIS] Cannot proceed. {governance['hemana']['result']}.")
        print(f"Constitutional grounds: {governance['hemana'].get('note', 'See HeMana scan results.')}")
        print("Synthesis will explain this with care, not refusal.\n")
        return None

    print("\n--- PHASE 04 — ROUTE ---")
    routing = phase_04_route(governance, interpretation, signal)

    print("\n--- PHASE 05 — OUTPUT ---")
    output = phase_05_output(interpretation, governance, routing, signal, north_star)

    print("\n--- PHASE 06 — RECORD ---")
    sgil_entry = phase_06_record(signal, interpretation, governance, routing, output)

    print("\n" + "═" * 60)
    print("  SYNTHESIS RUNTIME LOOP — COMPLETE")
    print(f"  Session: {session_id}")
    print(f"  SGIL:    {sgil_entry['id']}")
    print("═" * 60 + "\n")

    return {
        "session_id":    session_id,
        "output":        output,
        "sgil_entry":    sgil_entry,
        "governance":    governance,
    }


# ════════════════════════════════════════════════════════════════════
# EXAMPLE USAGE
# ════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    """
    Example: Run a single Synthesis session with Pātaka context.

    Prerequisites:
    - synthesis_protocol_manifest.json in working directory
    - core/synthesis_identity.yaml
    - governance/sacred_pou_governance.yaml

    In production, the Pātaka snapshot would be loaded automatically
    from the daily biometric pipeline (morning_drop_pipeline()).
    """

    pataka_context = {
        "traffic_signal": "green",
        "mauri_score":    78.4,
        "hrv_status":     "normal",
        "sleep_status":   "adequate",
        "readiness":      74,
        "flow_window":    True,
    }

    result = synthesis_runtime(
        raw_input="I want to think through the next phase of the HEP ecosystem — where should I focus first?",
        human_sovereign="Peter Makara",
        pataka_snapshot=pataka_context,
    )

    if result:
        print("Output ready for Peter.")
        print(f"SGIL entry: {result['sgil_entry']['id']} — Memory Mesh: {result['sgil_entry']['memory_mesh']}")

# Voice Degradation Domain — Negative Space Mapper Extension

**Extension type:** New detection domain  
**Target tool:** `negative_space_mapper.py` — `_check_voice_degradation_absences` method  
**Version:** 0.1  
**Date:** March 2026  
**Repo:** `richard-porter/negative-space-mapper`  
**Companion to:** [Permanent Tells v0.2](https://github.com/richard-porter/dimensional-authorship/blob/main/analysis/permanent-tells.md) | [Dimensional Voice Stamp v0.1](https://github.com/richard-porter/dimensional-authorship/blob/main/experiments/dimensional-voice-stamp-v01.md)

-----

## What This Domain Detects

The Voice Degradation Domain checks voice-critical documents for the absence of markers that distinguish human-governed authorship from AI-flattened or drift-contaminated output.

It does not evaluate whether a document is well-written. It does not assess quality, style, or craft. It names absences — specifically, the absences that matter when a document’s governing voice is under pressure from collaboration, emotional weight, or extended production.

The domain was developed from two sources: the vocal voice preservation literature (degradation modeling under compromised conditions) and the Tell Engine v2.1 empirical data from the Taller Shell Trilogy (dimensional-authorship/experiments/tell-engine-empirical-note.md). Both sources converge on the same finding: voice under pressure degrades in detectable ways, and the degradation leaves conspicuous absences, not just conspicuous presences.

-----

## Domain Table Entry

|Domain               |What It Looks For                                                                          |
|---------------------|-------------------------------------------------------------------------------------------|
|**Voice Degradation**|Characteristic anomalies, register variance across sections, productive incoherence signals|

-----

## Domain Signals — Activation Conditions

The Voice Degradation domain activates when a document contains signals from **at least two** of the following three categories. A single signal category is insufficient — the domain is designed for voice-critical documents specifically, and single-category activation produces false positives on documents where voice degradation checking is not relevant.

**Category A — Collaboration metadata**  
Terms: `Claude`, `ChatGPT`, `GPT`, `Gemini`, `Grok`, `co-author`, `AI-assisted`, `session`, `prompt`, `collaboration`, `human-AI`

Rationale: Explicit collaboration markers indicate the document was produced under conditions where AI participation could introduce register contamination or voice drift. This is the most structurally reliable activation signal — it does not depend on content interpretation.

**Category B — Emotional register signals**  
Terms: `grief`, `loss`, `mourning`, `pressure`, `urgency`, `crisis`, `exhaustion`, `fear`, `overwhelm`, `deadline`, `trauma`, `recovery`

Rationale: Emotional weight is the condition under which human voice is most likely to degrade — either through the author’s own compromised state, or through over-reliance on AI execution when the emotional material is hardest to write directly. Vocal voice preservation literature identifies emotional distress as the primary degradation condition; the written analog is the same.

**Category C — Genre signals**  
Terms: `novel`, `memoir`, `fiction`, `novella`, `narrative`, `personal essay`, `short story`, `creative nonfiction`, `trilogy`, `chapter`

Rationale: Voice-critical forms are the genres where degradation is most consequential and most detectable. Technical documents, reports, and instructional content are not voice-critical in the same way — uniform register is appropriate in those forms, not a signal of degradation.

**Two-category minimum rule:** A document containing only collaboration metadata but no emotional or genre signals (e.g., a technical spec with AI tool citations) should not trigger voice degradation checking. A document containing only grief language but no collaboration or genre signals (e.g., a clinical intake form) should not trigger. The two-category minimum is the scope limiter that prevents the false positive problem documented in the healthcare domain calibration issue (Negative Space Mapper governance, v1.0).

-----

## Domain Essentials — What the Mapper Flags as Missing

Once activated, the domain checks for three essentials. Each is flagged as OVERLOOKED if absent.

### Essential 1: Characteristic Anomalies

**What it is:** The productive errors, slightly broken patterns, and signature idiosyncrasies that define a voice rather than its average. Sentences that run too long for reasons the author could not fully articulate. Metaphors that are slightly off but emotionally precise. Structural choices that violate craft convention in ways that recur across the work.

**Why its absence is conspicuous:** AI optimizes toward means. It smooths anomalies because anomalies look like errors to a system trained on correctness. A voice-critical document with no characteristic anomalies — one that is too consistently competent, too clean in its transitions, too resolved in its metaphors — is missing the signal that a governing human intelligence was present and imperfect. The Tell Engine v2.1 flagged this directly: *“The prose is very consistently competent. There are relatively few ugly patches, accidental dead sentences, or truly awkward transitions. Human drafts often have more scar tissue.”*

**Absence classification:** OVERLOOKED if the document shows no productive errors across extended passages. DELIBERATE if the author has documented a discipline-based aesthetic that consciously eliminates surface anomalies (in which case, the absence is scoped out and the domain should not flag it).

**Provenance test:** Are there passages where the author appears to have chosen the emotionally precise option over the technically correct one? If no such passages exist in a long work, the absence is conspicuous.

-----

### Essential 2: Register Variance

**What it is:** Variation in voice register across sections of the document — the presence of passages that operate differently from each other in terms of emotional proximity, syntactic complexity, and tonal distance from the material.

**Why its absence is conspicuous:** Human-governed long-form work has a variegated register: sections where the author moves close to the material, sections where they pull back, sections where the AI’s execution clarity was appropriate and sections where it was humanized out. Uniform register across a long work is the AI exoskeleton problem made detectable — it is what happens when no governing intelligence decided what each section needed.

Tell 7 (Register Contamination Boundary) in the Permanent Tells framework makes the same observation from the other direction: the presence of managed register boundaries is a human signal. The *absence* of any register boundary management — a document that sounds the same throughout — is what the Mapper flags here.

**Absence classification:** OVERLOOKED in most cases. STRUCTURAL if the document’s genre requires uniform register (legal briefs, technical specifications) — in which case, the domain should not have activated on this document, and the two-category minimum rule should be reviewed.

**Provenance test:** Does the document contain at least two discernibly different registers across its sections? If the document sounds the same from first page to last, the absence is conspicuous.

-----

### Essential 3: Productive Incoherence Signals

**What it is:** Evidence that the author preserved unresolved tensions, contradictions, or ambivalences rather than smoothing them into settled positions. Questions the work raises but does not answer. Characters or arguments that contain genuine internal tension rather than synthesis.

**Why its absence is conspicuous:** AI resolves. Given a contradiction, it will smooth it — either by choosing one side, synthesizing a middle position, or containing the tension in a way that neutralizes it. A voice-critical document with no productive incoherence is a document where every contradiction was resolved, every ambivalence was settled, every question was answered. That is not what human authorship looks like when it is working on something real.

The Tell Engine v2.1 confirmed productive incoherence as a human-positive signal in the Taller Shell data — specifically the tonal volatility finding: *“Willing to be sentimental, embarrassing, grandiose, self-mocking, overextended, corrective.”* The inverse — a document that is tonally consistent and emotionally settled throughout — is the absence the Mapper flags here.

**Absence classification:** OVERLOOKED if the document contains no unresolved tensions in a domain where real unresolved tensions exist. DELIBERATE if the author’s documented aesthetic is one of resolution and synthesis — in which case the absence is scoped out.

**Provenance test:** Find the places where the work approaches its most charged material. Does it resolve cleanly or does it hold the tension? If every charged passage resolves cleanly, the absence is conspicuous.

-----

## Scope Limitation — When Not to Activate

This domain is designed for voice-critical documents produced under conditions of AI collaboration, emotional pressure, or extended production. It is not appropriate for:

- Technical documentation, reports, specifications, or instructional content — uniform register is correct in these forms, not a degradation signal
- Academic papers with established citation and argument conventions — productive incoherence is controlled by genre convention, not its absence
- Short-form content under approximately 2,000 words — characteristic anomalies and register variance require sufficient length to be detectable
- Documents where the author has explicitly documented a resolution-based aesthetic — the absence of productive incoherence is then DELIBERATE, not OVERLOOKED

If a document activates on only one signal category, apply this scope check before proceeding. The most likely false positive is a technically-written document that uses emotional language in its framing but is not a voice-critical work.

-----

## Implementation Notes

### Method signature (following existing domain pattern)

```python
def _check_voice_degradation_absences(self, text: str, absences: list) -> None:
    """
    Voice Degradation domain.
    Activates on documents with signals from at least two of three categories:
    collaboration metadata, emotional register signals, genre signals.
    Checks for: characteristic anomalies, register variance, productive incoherence.
    """
```

### Activation logic

```python
VOICE_DEGRADATION_SIGNALS = {
    "collaboration": [
        "claude", "chatgpt", "gpt", "gemini", "grok", "co-author",
        "ai-assisted", "session", "collaboration", "human-ai", "prompt"
    ],
    "emotional": [
        "grief", "loss", "mourning", "pressure", "urgency", "crisis",
        "exhaustion", "fear", "overwhelm", "deadline", "trauma", "recovery"
    ],
    "genre": [
        "novel", "memoir", "fiction", "novella", "narrative", "personal essay",
        "short story", "creative nonfiction", "trilogy", "chapter"
    ]
}

# Activate only if two or more signal categories match
categories_matched = sum(
    1 for category, terms in VOICE_DEGRADATION_SIGNALS.items()
    if any(term in text.lower() for term in terms)
)
if categories_matched >= 2:
    self._check_voice_degradation_absences(text, absences)
```

### Essential signals (absence detection)

```python
VOICE_DEGRADATION_ESSENTIALS = {
    "characteristic_anomalies": [
        "awkward", "unconventional", "idiosyncratic", "unexpected",
        "imprecise", "unresolved", "rough", "scar", "broken"
    ],
    "register_variance": [
        "shifts", "varies", "moves between", "pulls back", "approaches",
        "closer", "distance", "register", "intimate", "formal"
    ],
    "productive_incoherence": [
        "contradiction", "tension", "ambivalent", "uncertain", "unresolved",
        "paradox", "both", "neither", "simultaneously", "despite"
    ]
}
```

**Note on essential detection:** Unlike activation signals, essentials are detected by their *absence* — the mapper checks whether these signal clusters are present and flags when they are not. The confidence threshold for absence flagging should be calibrated against document length: a 500-word document that contains no productive incoherence signals is less suspicious than a 50,000-word novel with none.

-----

## Known Calibration Risks

**Risk 1 — Short document false negatives:** Characteristic anomalies and register variance require length to be detectable. The domain may produce false negatives on short documents even when degradation is present. Minimum recommended length: 2,000 words.

**Risk 2 — Genre term proximity false positives:** A document about fiction writing that is not itself fiction may activate on genre signals. The two-category minimum partially mitigates this, but a document about fiction writing that also discusses AI collaboration will activate. Manual scope review recommended in these cases.

**Risk 3 — Therapeutic and clinical content:** Documents that use grief and loss language in a clinical or supportive context are not voice-critical in the authorship sense. Emotional register signals are the activation category most vulnerable to this false positive. If a document activates on emotional + genre signals but appears to be clinical or instructional in structure, apply the scope limitation check before proceeding.

-----

## Relationship to Existing Ecosystem

|Voice Degradation Essential|Ecosystem connection                                                 |Where it shows up                                              |
|---------------------------|---------------------------------------------------------------------|---------------------------------------------------------------|
|Characteristic anomalies   |Dimensional Fidelity Scorer v0.2 — Rhythm Signature anomaly extension|Permanent Tells Tell 4 (productive incoherence) at metric level|
|Register variance          |Permanent Tells Tell 7 — Register Contamination Boundary             |Tell Engine v2.1 Run 1 vs Run 2 scoring gap                    |
|Productive incoherence     |Permanent Tells Tell 4                                               |Tell Engine v2.1 tonal volatility finding                      |

-----

## Version History

|Version|Date      |Notes                                                                                                                                                                                              |
|-------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0.1    |March 2026|Initial domain specification. Derived from vocal voice preservation degradation modeling and Tell Engine v2.1 empirical data. Two-category activation minimum added to address false positive risk.|

-----

## Open Questions for v0.2

1. **Length threshold:** What is the minimum document length below which the domain should not activate? Needs empirical calibration against known cases.
1. **Confidence scoring:** The existing mapper uses confidence thresholds (0.0–1.0). What confidence level should voice degradation absences carry relative to existing domains? Characteristic anomaly absence is arguably higher-confidence than productive incoherence absence, which is harder to detect from surface features alone.
1. **Multi-author documents:** The domain assumes a single governing voice. Collaborative human works (co-authored novels, ensemble memoirs) may legitimately lack register variance because multiple voices are being deliberately unified. A multi-author flag should suppress the register variance essential.

-----

*Voice Degradation Domain · v0.1 · Negative Space Mapper Extension*  
*Part of the Richard Porter AI Safety ecosystem · Frozen Kernel System*  
*They leave. The knowledge stays.*

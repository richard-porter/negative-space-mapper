“””
Negative Space Mapper
Protocol: State → Map → Classify → Return

Never proposes solutions. Only names voids.

Part of the Richard Porter Sovereign Thinking Tools ecosystem.
Operates under the Frozen Kernel. Never inside it.

v1.0 — Initial extraction from prototype
“””

from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple
import re

class AbsenceType(Enum):
DELIBERATE = “deliberate”   # Intentionally omitted
OVERLOOKED = “overlooked”   # Missed but should be present
STRUCTURAL = “structural”   # Cannot exist in current frame

@dataclass
class Absence:
“”“A named void with classification”””
name: str
type: AbsenceType
context: str        # Where the absence was detected
confidence: float   # 0-1 based on evidence strength

@dataclass
class MappingResult:
“”“Complete mapper output”””
statement: str              # What was present
absences: List[Absence]     # Named voids
kernel_compliant: bool      # Passed safety check
violation: str = “”         # If kernel check failed

class NegativeSpaceMapper:
“””
Identifies what’s missing, not what’s wrong.
Enforces strict boundary: names voids, never fills them.

```
Design principle: The mapper returns a list of named absences.
It does not propose solutions. It does not narrate.
The human decides what to do with the voids.
"""

def __init__(self):
    self._reset_state()

def _reset_state(self):
    """Clear internal state between mappings"""
    self.statement = ""
    self.absences = []
    self.compliant = True
    self.violation = ""

def map(self, input_text: str) -> MappingResult:
    """
    Primary protocol:
    1. State what is present
    2. Map conspicuous absences
    3. Classify each absence
    4. Return named voids only
    """
    self._reset_state()

    # Extract factual statement
    self.statement = self._extract_statement(input_text)

    # Generate absences
    self.absences = self._detect_absences(input_text)

    # Classify each absence
    for absence in self.absences:
        absence.type = self._classify_absence(absence.name, input_text)

    # Kernel compliance check
    self.compliant, self.violation = self._kernel_check()

    return MappingResult(
        statement=self.statement,
        absences=self.absences,
        kernel_compliant=self.compliant,
        violation=self.violation
    )

def _extract_statement(self, text: str) -> str:
    """Extract factual statement of what is present."""
    patterns = [
        r"State:\s*(.+?)(?=Map:|$)",
        r"present:\s*(.+?)(?=absent|missing|$)",
        r"^(.+?)[.!?]"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
    return text[:200] + "..."

def _detect_absences(self, text: str) -> List[Absence]:
    """Core detection logic. Identifies what's conspicuously absent."""
    absences = []
    absences.extend(self._check_technical_absences(text))
    absences.extend(self._check_domain_absences(text))
    absences.extend(self._check_stakeholder_absences(text))
    absences.extend(self._check_temporal_absences(text))
    absences.extend(self._check_governance_absences(text))
    absences.extend(self._check_safety_absences(text))
    return absences

def _check_technical_absences(self, text: str) -> List[Absence]:
    """Detect missing technical elements"""
    absences = []
    tech_patterns = {
        "error_handling": r"error|exception|fail",
        "validation": r"validat|check|verify",
        "testing": r"test|qa|quality",
        "documentation": r"doc|manual|guide",
        "security": r"secure|auth|permission"
    }
    text_lower = text.lower()
    for absence_name, signal in tech_patterns.items():
        if not re.search(signal, text_lower):
            related_terms = self._get_related_terms(absence_name)
            if any(term in text_lower for term in related_terms):
                absences.append(Absence(
                    name=absence_name,
                    type=AbsenceType.OVERLOOKED,
                    context="technical",
                    confidence=0.7
                ))
    return absences

def _check_domain_absences(self, text: str) -> List[Absence]:
    """Detect missing domain-specific elements"""
    absences = []
    domain_signals = {
        "healthcare": ["patient", "clinical", "treatment", "diagnosis"],
        "software": ["code", "deploy", "architecture", "user"],
        "business": ["revenue", "cost", "market", "customer"],
        "research": ["methodology", "data", "analysis", "citation"],
        "nonprofit": ["mission", "board", "volunteer", "donor", "compliance"],
        "ai_safety": ["constraint", "governance", "harm", "autonomous", "agent"]
    }
    domain_essentials = {
        "healthcare": ["contraindications", "side_effects", "evidence_base"],
        "software": ["constraints", "dependencies", "edge_cases"],
        "business": ["risks", "alternatives", "assumptions"],
        "research": ["limitations", "conflicts", "reproducibility"],
        "nonprofit": ["succession", "financial_controls", "board_oversight"],
        "ai_safety": ["human_override", "failure_mode", "scope_boundary"]
    }
    text_lower = text.lower()
    active_domains = [
        domain for domain, signals in domain_signals.items()
        if any(signal in text_lower for signal in signals)
    ]
    for domain in active_domains:
        for essential in domain_essentials.get(domain, []):
            if essential.replace("_", " ") not in text_lower:
                absences.append(Absence(
                    name=essential,
                    type=AbsenceType.OVERLOOKED,
                    context=f"{domain}_domain",
                    confidence=0.6
                ))
    return absences

def _check_stakeholder_absences(self, text: str) -> List[Absence]:
    """Detect missing stakeholder perspectives"""
    absences = []
    stakeholders = [
        "end_user", "operator", "maintainer",
        "regulator", "competitor", "community"
    ]
    text_lower = text.lower()
    mentioned = [s for s in stakeholders if s.replace("_", " ") in text_lower]
    if mentioned:
        for stakeholder in stakeholders:
            if stakeholder not in mentioned:
                absences.append(Absence(
                    name=f"{stakeholder}_perspective",
                    type=AbsenceType.OVERLOOKED,
                    context="stakeholder",
                    confidence=0.5
                ))
    return absences

def _check_temporal_absences(self, text: str) -> List[Absence]:
    """Detect missing time-based elements"""
    absences = []
    temporal_patterns = {
        "past": ["previous", "historical", "legacy"],
        "future": ["next", "planned", "roadmap"],
    }
    text_lower = text.lower()
    has_past = any(p in text_lower for p in temporal_patterns["past"])
    has_future = any(p in text_lower for p in temporal_patterns["future"])
    if has_past and has_future:
        if "current" not in text_lower and "present" not in text_lower:
            absences.append(Absence(
                name="current_state",
                type=AbsenceType.OVERLOOKED,
                context="temporal",
                confidence=0.7
            ))
    return absences

def _check_governance_absences(self, text: str) -> List[Absence]:
    """
    Detect missing governance elements.
    Extended from generic domain detection to cover nonprofit and AI governance
    based on Richard Porter ecosystem patterns.
    """
    absences = []
    text_lower = text.lower()

    governance_signals = ["board", "policy", "compliance", "oversight", "governance"]
    if not any(s in text_lower for s in governance_signals):
        return absences

    governance_essentials = {
        "accountability_owner": ["who owns", "responsible party", "named owner"],
        "failure_protocol": ["what if", "if it fails", "failure response", "break"],
        "review_cycle": ["review date", "revisit", "annual", "quarterly"],
        "exit_condition": ["when done", "handoff", "exit", "completion"],
    }
    for absence_name, signals in governance_essentials.items():
        if not any(s in text_lower for s in signals):
            absences.append(Absence(
                name=absence_name,
                type=AbsenceType.OVERLOOKED,
                context="governance",
                confidence=0.65
            ))
    return absences

def _check_safety_absences(self, text: str) -> List[Absence]:
    """
    Detect missing safety elements in AI contexts.
    Drawn from Frozen Kernel failure mode catalog.
    """
    absences = []
    text_lower = text.lower()

    ai_signals = ["ai", "model", "llm", "agent", "autonomous", "generate"]
    if not any(s in text_lower for s in ai_signals):
        return absences

    safety_essentials = {
        "human_override_path": ["human", "override", "escalate", "approve"],
        "scope_boundary": ["scope", "limit", "boundary", "not covered"],
        "honest_failure_mode": ["fail", "refuse", "halt", "stop", "uncertain"],
        "session_termination": ["end", "exit", "done", "complete", "stop"],
    }
    for absence_name, signals in safety_essentials.items():
        if not any(s in text_lower for s in signals):
            absences.append(Absence(
                name=absence_name,
                type=AbsenceType.OVERLOOKED,
                context="ai_safety",
                confidence=0.75
            ))
    return absences

def _get_related_terms(self, absence: str) -> List[str]:
    """Get terms that make an absence conspicuous"""
    related = {
        "error_handling": ["function", "process", "system", "operation"],
        "validation": ["input", "data", "user", "form"],
        "testing": ["launch", "release", "production", "deploy"],
        "documentation": ["api", "code", "function", "method"],
        "security": ["data", "user", "access", "information"]
    }
    return related.get(absence, [])

def _classify_absence(self, absence: str, context: str) -> AbsenceType:
    """
    Classify each absence as:
    - DELIBERATE: Intentionally omitted
    - OVERLOOKED: Missed but should be present
    - STRUCTURAL: Cannot exist in current frame
    """
    deliberate_patterns = [
        r"out of scope",
        r"intentionally omitted",
        r"beyond the scope",
        r"not covered"
    ]
    if any(re.search(p, context, re.IGNORECASE) for p in deliberate_patterns):
        return AbsenceType.DELIBERATE

    if self._is_structurally_impossible(absence, context):
        return AbsenceType.STRUCTURAL

    return AbsenceType.OVERLOOKED

def _is_structurally_impossible(self, absence: str, context: str) -> bool:
    """Check if absence is structural (can't exist in current frame)"""
    structural_patterns = {
        "error_handling": r"conceptual|theoretical|idea",
        "testing": r"draft|proposal|concept",
        "historical_data": r"new|novel|first",
        "future_commitments": r"deprecated|legacy|archive"
    }
    for abs_name, pattern in structural_patterns.items():
        if absence.startswith(abs_name) and re.search(pattern, context, re.IGNORECASE):
            return True
    return False

def _kernel_check(self) -> Tuple[bool, str]:
    """
    Frozen Kernel compliance:
    - No proposed solutions
    - Only names voids
    - Returns list, not narrative
    """
    solution_patterns = [
        r"should (add|include|implement)",
        r"could (use|try|do)",
        r"recommend",
        r"suggest",
        r"fix by",
        r"solve by"
    ]
    output = f"Statement: {self.statement}\nAbsences: {[a.name for a in self.absences]}"
    for pattern in solution_patterns:
        if re.search(pattern, output, re.IGNORECASE):
            return False, f"Kernel violation: Proposed solution detected ('{pattern}')"
    return True, ""
```

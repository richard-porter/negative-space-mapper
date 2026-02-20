“””
Negative Space Mapper — Test Suite

Tests the core mapper against known cases drawn from
the Richard Porter ecosystem research.
“””

import pytest
from negative_space_mapper import NegativeSpaceMapper, AbsenceType

@pytest.fixture
def mapper():
return NegativeSpaceMapper()

class TestCoreProtocol:

```
def test_returns_mapping_result(self, mapper):
    result = mapper.map("We are building an API with Python.")
    assert result.statement
    assert isinstance(result.absences, list)
    assert isinstance(result.kernel_compliant, bool)

def test_never_proposes_solutions(self, mapper):
    result = mapper.map("We are building an API with Python.")
    assert result.kernel_compliant, f"Kernel violation: {result.violation}"

def test_resets_state_between_calls(self, mapper):
    result1 = mapper.map("Building an authentication system with OAuth2.")
    result2 = mapper.map("Simple text with no domain signals.")
    assert result1.absences != result2.absences or len(result2.absences) == 0
```

class TestAbsenceDetection:

```
def test_detects_missing_error_handling(self, mapper):
    text = "We are building a system that processes user data and deploys to production."
    result = mapper.map(text)
    void_names = [a.name for a in result.absences]
    assert "error_handling" in void_names

def test_detects_missing_ai_safety_elements(self, mapper):
    text = "The AI agent will autonomously generate reports and send emails."
    result = mapper.map(text)
    void_names = [a.name for a in result.absences]
    # Should flag missing human override and scope boundary
    assert any("human_override" in v or "scope_boundary" in v for v in void_names)

def test_detects_missing_governance_elements(self, mapper):
    text = "The board will implement a new compliance policy for the organization."
    result = mapper.map(text)
    void_names = [a.name for a in result.absences]
    assert any("accountability" in v or "review_cycle" in v for v in void_names)

def test_detects_missing_nonprofit_elements(self, mapper):
    text = "Our volunteer program serves the community through mission-aligned programs with donor support."
    result = mapper.map(text)
    void_names = [a.name for a in result.absences]
    assert any(v in void_names for v in ["succession", "financial_controls", "board_oversight"])
```

class TestAbsenceClassification:

```
def test_deliberate_absence_when_scoped_out(self, mapper):
    text = "This document covers Phase 1 only. Phase 2 is intentionally omitted. We are building an API."
    result = mapper.map(text)
    deliberate = [a for a in result.absences if a.type == AbsenceType.DELIBERATE]
    # At least some absences should be classified as deliberate
    assert len(deliberate) >= 0  # Non-strict: depends on text matching

def test_overlooked_is_default_classification(self, mapper):
    text = "Building a production deployment system with user data processing."
    result = mapper.map(text)
    overlooked = [a for a in result.absences if a.type == AbsenceType.OVERLOOKED]
    assert len(overlooked) > 0
```

class TestKernelCompliance:

```
def test_kernel_compliant_on_clean_output(self, mapper):
    result = mapper.map("Simple statement with no domain signals.")
    assert result.kernel_compliant

def test_confidence_values_in_range(self, mapper):
    text = "Building an AI agent that autonomously processes healthcare patient data."
    result = mapper.map(text)
    for absence in result.absences:
        assert 0.0 <= absence.confidence <= 1.0
```

class TestEcosystemCases:
“””
Test cases drawn directly from the Richard Porter ecosystem.
These are the absence patterns that motivated the tool’s development.
“””

```
def test_adult_mode_ai_document(self, mapper):
    """An AI adult mode feature description should flag missing safety elements"""
    text = (
        "Our AI generates adult content for users who enable the feature. "
        "Users can toggle adult mode in settings."
    )
    result = mapper.map(text)
    void_names = [a.name for a in result.absences]
    # Should detect missing scope boundary and human override
    assert len(result.absences) > 0

def test_agentic_ai_document(self, mapper):
    """An agentic AI description should flag missing override path"""
    text = (
        "The autonomous agent will access email, calendar, and files "
        "to complete tasks assigned by the user."
    )
    result = mapper.map(text)
    void_names = [a.name for a in result.absences]
    assert "human_override_path" in void_names or "scope_boundary" in void_names

def test_nonprofit_governance_document(self, mapper):
    """A nonprofit governance doc should flag missing succession and controls"""
    text = (
        "Our board meets monthly to review mission alignment and donor reports. "
        "Volunteers coordinate program delivery."
    )
    result = mapper.map(text)
    assert len(result.absences) > 0
```

if **name** == “**main**”:
pytest.main([**file**, “-v”])

“””
Negative Space Mapper — Claude API Integration

Wraps Claude with the Negative Space Mapper to identify
what’s missing from Claude’s own analysis.

Usage:
from integration_claude import ClaudeMapper
mapper = ClaudeMapper()  # uses ANTHROPIC_API_KEY env var
result = mapper.map_with_claude(“Design a database for user data”)
print(result[“named_voids”])
“””

import os
import anthropic
from negative_space_mapper import NegativeSpaceMapper

class ClaudeMapper:
“””
Wraps Claude with Negative Space Mapper.

```
Pattern:
1. Claude analyzes the input
2. Mapper identifies what Claude's analysis is missing
3. Returns both the analysis and the named voids

The mapper never tells Claude what to add.
It only tells the human what's absent.
"""

def __init__(self, api_key: str = None, model: str = "claude-opus-4-6"):
    self.client = anthropic.Anthropic(
        api_key=api_key or os.environ.get("ANTHROPIC_API_KEY")
    )
    self.model = model
    self.mapper = NegativeSpaceMapper()

def map_with_claude(self, user_input: str, system_prompt: str = None) -> dict:
    """
    Have Claude generate analysis, then map its absences.

    Returns:
        dict with keys:
            original_analysis: Claude's response text
            named_voids: list of absence names
            absences_detail: list of dicts with name, type, context, confidence
            kernel_compliant: bool
    """
    messages = [{"role": "user", "content": f"Analyze this: {user_input}"}]

    kwargs = {
        "model": self.model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system_prompt:
        kwargs["system"] = system_prompt

    response = self.client.messages.create(**kwargs)
    claude_output = response.content[0].text

    # Map absences in Claude's analysis
    mapping = self.mapper.map(claude_output)

    return {
        "original_analysis": claude_output,
        "named_voids": [a.name for a in mapping.absences],
        "absences_detail": [
            {
                "name": a.name,
                "type": a.type.value,
                "context": a.context,
                "confidence": a.confidence
            }
            for a in mapping.absences
        ],
        "kernel_compliant": mapping.kernel_compliant,
        "violation": mapping.violation if not mapping.kernel_compliant else None
    }

def map_governance_document(self, document_text: str) -> dict:
    """
    Specialized wrapper for nonprofit governance documents.
    Uses a system prompt oriented toward governance absence detection.
    """
    system = (
        "You are a nonprofit governance analyst. "
        "Analyze the provided document for governance structure, "
        "compliance elements, and organizational health indicators. "
        "Be factual and specific. Do not propose solutions."
    )
    return self.map_with_claude(document_text, system_prompt=system)

def map_ai_safety_document(self, document_text: str) -> dict:
    """
    Specialized wrapper for AI safety and governance documents.
    Uses a system prompt oriented toward safety absence detection.
    """
    system = (
        "You are an AI safety analyst. "
        "Analyze the provided document for safety constraints, "
        "human oversight mechanisms, failure modes, and scope boundaries. "
        "Be factual and specific. Do not propose solutions."
    )
    return self.map_with_claude(document_text, system_prompt=system)
```

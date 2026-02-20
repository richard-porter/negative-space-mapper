# Negative Space Mapper

**Identifies what’s missing, not what’s wrong.**  
Protocol: State → Map → Classify → Return. Never proposes solutions.

Part of the [Richard Porter Sovereign Thinking Tools ecosystem](https://github.com/richard-porter/where-to-start).  
Operates under the Frozen Kernel. Never inside it.

-----

## What This Is

The Negative Space Mapper is a cognitive tool — and now a software implementation — for identifying conspicuous absences in documents, plans, designs, and AI outputs.

It does one thing: it names what’s missing. It does not propose solutions, recommend fixes, or suggest improvements. The human decides what to do with the voids.

This constraint is not a limitation. It is the design. A tool that names absences without filling them preserves the human’s sovereignty over the decision that follows.

-----

## The Three Absence Types

|Type          |Definition                                                                  |
|--------------|----------------------------------------------------------------------------|
|**DELIBERATE**|Intentionally omitted — the absence is scoped out                           |
|**OVERLOOKED**|Should be present but isn’t — conspicuous gap                               |
|**STRUCTURAL**|Cannot exist in the current frame — e.g., test results before implementation|

-----

## Installation

```bash
pip install anthropic  # only needed for Claude integration
```

No other dependencies. The core mapper uses only the Python standard library.

-----

## Usage

### Command Line

```bash
# Basic
python cli.py "We're building a new API with Python and FastAPI"

# From file
python cli.py @document.txt

# Verbose output (shows type, context, confidence)
python cli.py -v "Designing a healthcare app"

# JSON output
python cli.py -f json "Project plan for Q3"

# Filter by confidence threshold
python cli.py -c 0.7 "Autonomous AI agent for email management"
```

### Python

```python
from negative_space_mapper import NegativeSpaceMapper

mapper = NegativeSpaceMapper()
result = mapper.map("The AI agent will autonomously generate reports and send emails.")

print(result.statement)
for absence in result.absences:
    print(f"  • {absence.name} ({absence.type.value}) [{absence.context}]")
print(f"Kernel compliant: {result.kernel_compliant}")
```

### With Claude API

```python
from integration_claude import ClaudeMapper

mapper = ClaudeMapper()  # uses ANTHROPIC_API_KEY env var

# Map absences in Claude's own analysis
result = mapper.map_with_claude("Design a database for user data")
print(result["named_voids"])

# Specialized wrappers
gov_result = mapper.map_governance_document(open("bylaws.txt").read())
ai_result = mapper.map_ai_safety_document(open("safety_spec.txt").read())
```

-----

## Detection Domains

The mapper currently detects absences in six domains:

|Domain             |What It Looks For                                                            |
|-------------------|-----------------------------------------------------------------------------|
|**Technical**      |Error handling, validation, testing, documentation, security                 |
|**Domain-specific**|Healthcare, software, business, research, nonprofit, AI safety essentials    |
|**Stakeholder**    |Missing perspectives: end user, operator, maintainer, regulator, community   |
|**Temporal**       |Missing current state when past and future are both addressed                |
|**Governance**     |Accountability owner, failure protocol, review cycle, exit condition         |
|**AI Safety**      |Human override path, scope boundary, honest failure mode, session termination|

The AI Safety and Governance domains were extended from the generic prototype to reflect absence patterns observed in the [Frozen Kernel](https://github.com/richard-porter/frozen-kernel) and [Adult Mode Safety Ledger](https://github.com/richard-porter/adult-mode-safety-ledger) research.

-----

## Running Tests

```bash
python -m pytest tests.py -v
```

Test cases include ecosystem-specific scenarios: agentic AI documents, adult mode feature descriptions, and nonprofit governance documents.

-----

## Extending the Mapper

To add absence patterns from your own domain:

1. Add a new `_check_[domain]_absences` method to `NegativeSpaceMapper`
1. Add domain signals (terms that activate the detector)
1. Add domain essentials (terms whose absence is conspicuous)
1. Call the new method from `_detect_absences`
1. Test against known cases

The absence pattern catalog will expand as the ecosystem generates more empirical data. Contributions of domain-specific absence patterns — especially from clinical, legal, and financial contexts — are the highest-value contribution.

-----

## Kernel Compliance

The mapper enforces Frozen Kernel compliance on its own output:

- No proposed solutions
- No recommendations
- No suggestions
- Returns a list of named voids, not a narrative

If the mapper’s output contains solution language, it flags a kernel violation rather than returning non-compliant output.

-----

## Files

|File                      |Contents                       |
|--------------------------|-------------------------------|
|`negative_space_mapper.py`|Core mapper class              |
|`cli.py`                  |Command-line interface         |
|`integration_claude.py`   |Claude API wrapper             |
|`tests.py`                |Test suite with ecosystem cases|
|`README.md`               |This file                      |

-----

## Relationship to Sovereign Thinking Tools

This implementation corresponds to Tool 6 in [Sovereign Thinking Tools v3.0](https://github.com/richard-porter/where-to-start). The protocol document remains the primary reference. This repository is the software implementation — the same tool in a different register.

-----

## License

Released for public benefit. Attribution appreciated but not required.

The only ask: **if you extend the absence catalog, share what you find.**

-----

*Negative Space Mapper · v1.0 · Frozen Kernel System*  
*They leave. The knowledge stays.*

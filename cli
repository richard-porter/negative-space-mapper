#!/usr/bin/env python3
“””
Command-line Negative Space Mapper

Usage:
python cli.py “We’re building a new API with Python and FastAPI”
python cli.py @document.txt
python cli.py -v “Designing a healthcare app”
python cli.py -f json “Project plan for Q3”
“””

import argparse
import sys
import json
from pathlib import Path
from negative_space_mapper import NegativeSpaceMapper

def main():
parser = argparse.ArgumentParser(
description=“Negative Space Mapper — Identify what’s missing, not what’s wrong”,
epilog=“Part of the Richard Porter Sovereign Thinking Tools ecosystem.”
)
parser.add_argument(
“input”,
help=“Input text or @filename to read from file”
)
parser.add_argument(
“–format”, “-f”,
choices=[“text”, “json”],
default=“text”,
help=“Output format (default: text)”
)
parser.add_argument(
“–verbose”, “-v”,
action=“store_true”,
help=“Show absence type, context, and confidence”
)
parser.add_argument(
“–min-confidence”, “-c”,
type=float,
default=0.0,
help=“Minimum confidence threshold for absences (0.0-1.0)”
)

```
args = parser.parse_args()

# Read input
if args.input.startswith('@'):
    path = Path(args.input[1:])
    if not path.exists():
        print(f"Error: File {path} not found", file=sys.stderr)
        sys.exit(1)
    text = path.read_text()
else:
    text = args.input

# Map
mapper = NegativeSpaceMapper()
result = mapper.map(text)

# Filter by confidence
filtered_absences = [
    a for a in result.absences
    if a.confidence >= args.min_confidence
]

# Output
if args.format == "json":
    output = {
        "statement": result.statement,
        "absences": [
            {
                "name": a.name,
                "type": a.type.value,
                "context": a.context,
                "confidence": a.confidence
            }
            for a in filtered_absences
        ],
        "kernel_compliant": result.kernel_compliant,
        "violation": result.violation if not result.kernel_compliant else None
    }
    print(json.dumps(output, indent=2))

else:
    print(f"\nSTATEMENT:\n{result.statement}\n")
    print("NAMED VOIDS:")
    if filtered_absences:
        for a in filtered_absences:
            if args.verbose:
                print(f"  • {a.name}")
                print(f"    type: {a.type.value} | context: {a.context} | confidence: {a.confidence:.0%}")
            else:
                print(f"  • {a.name}")
    else:
        print("  (none detected)")

    if not result.kernel_compliant:
        print(f"\n⚠️  KERNEL VIOLATION: {result.violation}")
    else:
        print(f"\n✓ Kernel compliant")
```

if **name** == “**main**”:
main()

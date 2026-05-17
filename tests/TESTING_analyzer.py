import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.distress import analyze_distress

test_messages = [
    "I'm feeling great today, just had a nice walk!",
    "I've been really stressed about my exams lately.",
    "I can't stop crying and I feel completely alone.",
    "I don't see the point in anything anymore. Nothing matters.",
    "I want to hurt myself. I can't take this pain anymore."
]

print("=" * 55)
print("  DISTRESS ANALYZER — TEST RUN")
print("=" * 55)

for msg in test_messages:
    print(f"\n📨 Message: {msg}")
    result = analyze_distress(msg)
    severity = result.get("severity", "?")
    emotions = result.get("emotions", [])
    summary = result.get("summary", "")

    # visual severity bar
    bar = "█" * severity + "░" * (5 - severity)
    print(f"   Severity : [{bar}] {severity}/5")
    print(f"   Emotions : {', '.join(emotions)}")
    print(f"   Summary  : {summary}")
    print("-" * 55)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.distress import analyze_distress
from tools.router import route

messages = [
    "Just had a productive day!",
    "Feeling a bit anxious about tomorrow.",
    "I've been crying all day and I don't know why.",
    "I feel completely hopeless. Nothing is working out.",
    "I don't want to live anymore."
]

print("=" * 60)
print("  TRIAGE ROUTER — FULL PIPELINE TEST")
print("=" * 60)

for msg in messages:
    print(f"\n📨 {msg}")
    analysis = analyze_distress(msg)
    result = route(analysis)

    print(f"   Severity : {analysis['severity']}/5")
    print(f"   Emotions : {', '.join(analysis['emotions'])}")
    print(f"   Route    : {result['level'].upper()}")
    print(f"   Resources: {len(result['resources'])} item(s) queued")
    print("-" * 60)
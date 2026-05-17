import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.distress import analyze_distress
from tools.router import route
from agent.session_mem import SessionMemory
from agent.response_composer import compose_response

memory = SessionMemory()

test_conversation = [
    "I've been feeling really anxious lately, can't sleep.",
    "It's getting worse. I feel completely hopeless.",
    "I don't want to be here anymore."
]

print("=" * 60)
print("  FULL PIPELINE — END TO END TEST")
print("=" * 60)

for user_msg in test_conversation:
    print(f"\n👤 User: {user_msg}\n")

    # step 1 — analyze
    analysis = analyze_distress(user_msg)

    # step 2 — route
    triage = route(analysis)

    # step 3 — check escalation
    if memory.should_escalate():
        triage = route({"severity": 5, "emotions": analysis["emotions"]})

    # step 4 — compose
    response = compose_response(
        user_message=user_msg,
        analysis=analysis,
        route=triage,
        memory_context=memory.get_context_summary(),
        chat_history=memory.get_chat_history()
    )

    # step 5 — store turn
    memory.add_turn(user_msg, analysis, response)

    print(f"🤖 Agent [{triage['level'].upper()}]:\n")
    print(response)
    print("\n" + "=" * 60)
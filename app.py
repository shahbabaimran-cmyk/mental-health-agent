import streamlit as st
from agent.distress import analyze_distress
from tools.router import route
from agent.session_mem import SessionMemory
from agent.response_composer import compose_response

# ── Page config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Mental Health First Responder",
    page_icon="🧠",
    layout="wide"
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    .severity-bar { height: 8px; border-radius: 4px; margin: 4px 0; }
    .level-calm      { color: #4ade80; font-weight: 600; }
    .level-support   { color: #facc15; font-weight: 600; }
    .level-coping    { color: #fb923c; font-weight: 600; }
    .level-crisis    { color: #f87171; font-weight: 600; }
    .level-emergency { color: #dc2626; font-weight: 700; }
    .disclaimer {
        font-size: 11px;
        color: #6b7280;
        text-align: center;
        padding: 8px;
        border-top: 1px solid #1f2937;
        margin-top: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────
if "memory" not in st.session_state:
    st.session_state.memory = SessionMemory()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of (role, content, meta)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧠 Mental Health\nFirst Responder Agent")
    st.markdown("---")

    # mood trend chart
    memory = st.session_state.memory
    if memory.severity_log:
        st.markdown("### 📊 Mood Trend")
        chart_data = {"Severity": memory.severity_log}
        st.line_chart(chart_data, color="#818cf8")

        # current stats
        trend = memory.get_trend()
        avg = sum(memory.severity_log) / len(memory.severity_log)
        last = memory.severity_log[-1]

        trend_icon = {"worsening": "📈", "improving": "📉", "stable": "➡️"}.get(trend, "➡️")

        st.markdown(f"""
| Metric | Value |
|---|---|
| Current severity | {last}/5 |
| Average | {avg:.1f}/5 |
| Trend | {trend_icon} {trend.capitalize()} |
| Turns | {len(memory.severity_log)} |
""")

    else:
        st.markdown("*Mood chart will appear after your first message.*")

    st.markdown("---")

    # reset button
    if st.button("🔄 Start new session"):
        st.session_state.memory = SessionMemory()
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("""
<div class="disclaimer">
⚠️ This is an AI support tool, not a replacement for professional mental health care.
If you are in immediate danger, please call emergency services.
</div>
""", unsafe_allow_html=True)

# ── Main chat area ───────────────────────────────────────────
st.markdown("## 💬 How are you feeling today?")
st.markdown("*This is a safe space. Share whatever is on your mind.*")
st.markdown("---")

# render chat history
for role, content, meta in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    else:
        with st.chat_message("assistant", avatar="🧠"):
            st.markdown(content)
            if meta:
                level = meta.get("level", "calm")
                severity = meta.get("severity", 1)
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(
                        f"<span class='level-{level}'>● {level.upper()}</span>",
                        unsafe_allow_html=True
                    )
                with col2:
                    bar_color = {
                        1: "#4ade80", 2: "#a3e635",
                        3: "#facc15", 4: "#fb923c", 5: "#dc2626"
                    }.get(severity, "#818cf8")
                    bar_width = severity * 20
                    st.markdown(
                        f"<div class='severity-bar' style='width:{bar_width}%; background:{bar_color}'></div>",
                        unsafe_allow_html=True
                    )

# ── Chat input ───────────────────────────────────────────────
user_input = st.chat_input("Type how you're feeling...")

if user_input:
    # show user message immediately
    st.session_state.chat_history.append(("user", user_input, None))

    with st.chat_message("user"):
        st.markdown(user_input)

    # run the agent pipeline
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Thinking..."):
            memory = st.session_state.memory

            # pipeline
            analysis = analyze_distress(user_input)
            triage = route(analysis)

            # auto-escalate if trend demands it
            if memory.should_escalate():
                triage = route({"severity": 5, "emotions": analysis["emotions"]})

            response = compose_response(
                user_message=user_input,
                analysis=analysis,
                route=triage,
                memory_context=memory.get_context_summary(),
                chat_history=memory.get_chat_history()
            )

            memory.add_turn(user_input, analysis, response)

        # display response
        st.markdown(response)

        level = triage.get("level", "calm")
        severity = analysis.get("severity", 1)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(
                f"<span class='level-{level}'>● {level.upper()}</span>",
                unsafe_allow_html=True
            )
        with col2:
            bar_color = {
                1: "#4ade80", 2: "#a3e635",
                3: "#facc15", 4: "#fb923c", 5: "#dc2626"
            }.get(severity, "#818cf8")
            bar_width = severity * 20
            st.markdown(
                f"<div class='severity-bar' style='width:{bar_width}%; background:{bar_color}'></div>",
                unsafe_allow_html=True
            )

        # store in chat history
        st.session_state.chat_history.append((
            "assistant", response, {"level": level, "severity": severity}
        ))

    st.rerun()
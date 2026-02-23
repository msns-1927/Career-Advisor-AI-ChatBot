import streamlit as st
from gemini_client import GeminiClient
from prompt_manager import PromptManager
from memory import ChatMemory
from config import Config

# Page configuration
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="💼",
    layout="centered"
)

st.title("💼 AI Career Advisor")
st.markdown("Structured career guidance powered by Gemini AI.")

# Initialize client and session memory
client = GeminiClient()

if "memory" not in st.session_state:
    st.session_state.memory = ChatMemory()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous chat messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Chat input
user_input = st.chat_input("Ask your career-related question...")

if user_input:

    # Display user message
    st.session_state.chat_history.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Guardrail check
    is_career = client.classify_career_query(user_input)

    if not is_career:
        warning_msg = "⚠️ I provide career-related guidance only."
        with st.chat_message("assistant"):
            st.markdown(warning_msg)

        st.session_state.chat_history.append(("assistant", warning_msg))

    else:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing and generating structured guidance..."):

                prompt = PromptManager.build_prompt(
                    user_input,
                    st.session_state.memory.get_history()
                )

                response = client.generate_response(prompt)

                if isinstance(response, dict):

                    output = f"""
### 🎯 Career Guidance
{response.get("career_guidance", "")}

### 📚 Skills to Develop
{"".join(f"- {s}\n" for s in response.get("skills_to_develop", []))}

### 🛠 Recommended Actions
{"".join(f"- {a}\n" for a in response.get("recommended_actions", []))}

### 🚀 Step-by-Step Plan
{"".join(f"- {s}\n" for s in response.get("step_by_step_plan", []))}
"""
                else:
                    output = response

                st.markdown(output)

        # Save history
        st.session_state.chat_history.append(("assistant", output))
        st.session_state.memory.add(user_input, output)

# ---------------- Sidebar ----------------
st.sidebar.title("⚙️ Settings")

# Display token usage
if "token_usage" not in st.session_state:
    st.session_state.token_usage = {
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0
    }

st.sidebar.markdown("### 📊 Token Usage")

st.sidebar.metric(
    "Input Tokens",
    st.session_state.token_usage["input_tokens"]
)

st.sidebar.metric(
    "Output Tokens",
    st.session_state.token_usage["output_tokens"]
)

st.sidebar.metric(
    "Total Tokens",
    st.session_state.token_usage["total_tokens"]
)

# Reset button
if st.sidebar.button("🔄 Reset Conversation"):
    st.session_state.chat_history = []
    st.session_state.memory = ChatMemory()
    st.session_state.token_usage = {
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0
    }
    st.rerun()
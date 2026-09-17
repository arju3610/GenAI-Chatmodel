import streamlit as st
import httpx
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


# ---------------- MODEL ----------------
model = ChatGroq(model="openai/gpt-oss-20b",temperature=0.9)


# ---------------- PAGE ----------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mood Based AI Chatbot")
st.caption("Choose AI personality and start chatting | Type 0 to stop")


# ---------------- MODE SELECTION ----------------
mode_choice = st.radio(
    "Choose your AI Mode:",
    ["😡 Angry", "😂 Funny", "😢 Sad"],
    horizontal=True
)


# Map mode
if mode_choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."


# ---------------- SESSION MEMORY ----------------
if "messages" not in st.session_state or st.session_state.get("current_mode") != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [SystemMessage(content=mode)]


# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)


# ---------------- USER INPUT ----------------
user_input = st.chat_input("Say something...")

if user_input:

    if user_input == "0":
        st.warning("Conversation ended. Refresh page to start again.")
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        try:
            response = model.invoke(st.session_state.messages)
        except httpx.HTTPStatusError as error:
            # Do not retain an unanswered prompt; otherwise it would be sent again
            # along with the user's next message.
            st.session_state.messages.pop()

            if error.response.status_code == 429:
                st.warning(
                    "Mistral's API rate limit has been reached. Please wait a moment "
                    "before trying again, or check your Mistral account's quota."
                )
            else:
                st.error(f"Mistral API request failed (HTTP {error.response.status_code}).")
        except Exception:
            st.session_state.messages.pop()
            st.error("The AI response could not be generated. Please try again.")
        else:
            st.session_state.messages.append(AIMessage(content=response.content))
            st.write(response.content)


# ---------------- CLEAR BUTTON ----------------
st.divider()
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=mode)]
    st.rerun()

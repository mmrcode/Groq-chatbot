import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Early check for GROQ API key to give immediate UI feedback
if not os.getenv("GROQ_API_KEY"):
    st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
    st.title("🤖 Groq AI Chatbot")
    st.sidebar.error("GROQ_API_KEY is not set")
    st.markdown(
        "**GROQ_API_KEY is not set.**\n\nCopy `.env.example` to `.env` and set `GROQ_API_KEY`, or set the `GROQ_API_KEY` environment variable before running the app."
    )
    st.markdown(
        "1. Copy `.env.example` to `.env`.\n"
        "2. Add your Groq API key: `GROQ_API_KEY=your_key_here`.\n"
        "3. Restart the app."
    )
    st.stop()

from services.groq_service import get_chat_response, stream_chat_response

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq AI Chatbot")

# Sidebar controls
st.sidebar.title("⚙️ Settings")
streaming_enabled = st.sidebar.checkbox("Enable Streaming", value=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask something..."):
    # Store & show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        try:
            if streaming_enabled:
                response_box = st.empty()
                full_response = ""

                for token in stream_chat_response(st.session_state.messages):
                    full_response += token
                    response_box.markdown(full_response)

            else:
                full_response = get_chat_response(st.session_state.messages)
                st.markdown(full_response)

        except Exception as e:
            full_response = f"Error: {e}"
            st.markdown(full_response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_response})

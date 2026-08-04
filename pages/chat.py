import streamlit as st
from utils.gemini import get_gemini_response

st.set_page_config(page_title="Cyber AI Chat")

st.title("💬 CyberGuard AI Chat")

st.write("Ask me anything about cybersecurity!")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Ask a cybersecurity question...")

if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🛡️ CyberGuard AI is Thinking..."):

            answer = get_gemini_response(prompt)

            st.markdown(answer)

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

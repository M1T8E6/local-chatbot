import streamlit as st

from scripts.sidebar import get_llm_and_sidebar

# Initialize the LLM with sidebar configuration
llm = get_llm_and_sidebar()

# Title and session state initialization
st.title("My Local GPT 🤭")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input handling
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Stream the assistant's response
        stream = llm.stream(
            input=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        response = st.write_stream(stream)

    # Store the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st
from langchain_ollama import ChatOllama


# Function to create sliders for numerical inputs
def create_slider(label, min_val, max_val, default_val, step=0.1):
    """
    Creates a slider in the Streamlit sidebar.
    """
    return st.sidebar.slider(
        label, min_value=min_val, max_value=max_val, value=default_val, step=step
    )


# Function to create number inputs
def create_number_input(label, min_val, default_val):
    """
    Creates a number input field in the sidebar of a Streamlit app.
    """
    return st.sidebar.number_input(label, min_value=min_val, value=default_val)


# Function to create model configuration sidebar
def get_llm_and_sidebar():
    """
    Creates a sidebar in the Streamlit app for configuring the language model parameters and returns an instance of ChatOllama with the selected configurations.
    """
    st.sidebar.title("Model Configurations")

    model_type = st.sidebar.selectbox(
        "Model Type", ["deepseek-coder:33b", "llama3", "codellama:13b"]
    )

    mirostat = st.sidebar.selectbox("Mirostat", [None, 0, 1, 2], index=0)
    mirostat_eta = create_slider("Mirostat Eta", 0.0, 1.0, 0.1)
    mirostat_tau = create_slider("Mirostat Tau", 0.0, 10.0, 5.0)

    num_ctx = create_number_input("Context Size (num_ctx)", 1, 2048)
    num_gpu = create_number_input("Number of GPUs (num_gpu)", 0, 1)
    num_thread = create_number_input("Number of Threads (num_thread)", 1, 4)
    num_predict = create_number_input(
        "Number of Tokens to Predict (num_predict)", -2, 128
    )

    repeat_last_n = create_number_input("Repeat Last N Tokens (repeat_last_n)", -1, 64)
    repeat_penalty = create_slider("Repeat Penalty", 0.0, 2.0, 1.1)
    temperature = create_slider("Temperature", 0.0, 1.0, 0.8, 0.01)
    seed = create_number_input("Seed", 0, 0)

    stop = st.sidebar.text_area("Stop Tokens (separate by commas)", value="")
    stop_tokens = [token.strip() for token in stop.split(",")] if stop else None

    tfs_z = create_slider("TFS Z", 0.0, 5.0, 1.0)
    top_k = create_number_input("Top-K", 0, 40)
    top_p = create_slider("Top-P", 0.0, 1.0, 0.9, 0.01)

    # Return the LLM instance with all parameters
    return ChatOllama(
        model=model_type,
        temperature=temperature,
        mirostat=mirostat,
        mirostat_eta=mirostat_eta,
        mirostat_tau=mirostat_tau,
        num_ctx=num_ctx,
        num_gpu=num_gpu,
        num_thread=num_thread,
        num_predict=num_predict,
        repeat_last_n=repeat_last_n,
        repeat_penalty=repeat_penalty,
        seed=seed if seed > 0 else None,
        stop=stop_tokens,
        tfs_z=tfs_z,
        top_k=top_k,
        top_p=top_p,
    )

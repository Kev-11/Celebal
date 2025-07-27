import streamlit as st
import pandas as pd
from embedder import Embedder
from vectorstore import VectorStore
from retriever import Retriever
from generator import Generator
from rag_chain import RAGChain

# ----- Custom CSS styling -----
custom_css = """
<style>
.stChatMessage { margin-bottom: 1.2em; }
.user-bubble { background: #521F14; padding: 1em 1.2em; border-radius: 16px 16px 0 16px; max-width: 70%; margin-left: auto; }
.bot-bubble  { background: #FFFFFF; padding: 1em 1.2em; border-radius: 16px 16px 16px 0; max-width: 70%; margin-right: auto; }
.st-emotion-cache-1v0mbdj { max-height: 60vh; overflow-y: auto; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.set_page_config(page_title="Loan RAG Chatbot", page_icon="💬", layout="wide")

st.title("💬 Loan Approval Q&A Chatbot")
st.caption("Retrieval Augmented Generation (RAG) with Hugging Face models, FAISS, and your loan dataset.")

# Sidebar controls
with st.sidebar:
    st.header("🔧 Settings")
    uploaded_file = st.file_uploader("Upload Loan CSV", type="csv")
    model_choice = st.selectbox("LLM model", ["TinyLlama/TinyLlama-1.1B-Chat-v1.0", "OtherLocalModel"])
    top_k = st.slider("Number of relevant results to retrieve", 1, 10, 3)
    temperature = st.slider("LLM Temperature", 0.0, 1.0, 0.2)
    st.markdown("---")
    with st.expander("ℹ️ Dataset Info"):
        st.write("This chatbot answers questions about loan approvals from your uploaded dataset using Retrieval Augmented Generation (RAG).")

@st.cache_resource(show_spinner="Indexing dataset, please wait...")
def setup_rag_pipeline(csv_file, model_name, top_k):
    if isinstance(csv_file, str):
        docs = pd.read_csv(csv_file).astype(str).apply(lambda row: " ".join(row), axis=1).tolist()
    else:
        df = pd.read_csv(csv_file)
        docs = df.astype(str).apply(lambda row: " ".join(row), axis=1).tolist()
    embedder = Embedder()
    vectors = embedder.embed(docs)
    vectorstore = VectorStore(vectors.shape[1])
    vectorstore.add(vectors, docs)
    retriever = Retriever(embedder, vectorstore)
    generator = Generator(model_name=model_name)
    rag = RAGChain(retriever, generator)
    return rag

rag = setup_rag_pipeline(
    uploaded_file if uploaded_file else "Training Dataset.csv",
    model_choice,
    top_k,
)

# --- Conversation state ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Chat display & input ---
st.markdown("### Chat")
chat_placeholder = st.container()

with chat_placeholder:
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            with st.chat_message("user", avatar="🧑"):
                st.markdown(f"<div class='user-bubble'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(f"<div class='bot-bubble'>{message['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("Type your question about loan approval...")

if prompt:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            # Retrieve & generate answer
            answer = rag.answer(prompt)
            st.session_state["messages"].append({"role": "assistant", "content": answer})
            st.markdown(f"<div class='bot-bubble'>{answer}</div>", unsafe_allow_html=True)

st.divider()

st.markdown("##### Pro tip:")
st.markdown("- Upload your own dataset for custom Q&A\n- Change model/parameters in the sidebar\n- All processing happens locally (except model download on first use)")

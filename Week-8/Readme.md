# RAG Q&A Chatbot using Document Retrieval and Generative AI

This project implements a **Retrieval-Augmented Generation (RAG) Question Answering chatbot** that retrieves relevant information from a dataset and uses a generative language model to produce intelligent, context-aware answers.

---

## Project Structure

- `embedder.py`: Embeds text snippets using SentenceTransformers.
- `vectorstore.py`: Implements a FAISS vector store for similarity search.
- `retriever.py`: Retrieves relevant document chunks based on query embedding.
- `generator.py`: Generates answers using a Hugging Face text-generation model.
- `rag_chain.py`: Combines retrieval and generation into a coherent Q&A flow.
- `main.py`: Entry point script that loads data, builds index, and runs interactive chat.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Training Dataset.csv](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction?select=Training+Dataset.csv) (Place in project directory)

### Installation

1. Create and activate a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate # On Windows use venv\Scripts\activate

2. Install required packages:

    pip install -r requirements.txt

### Usage

Run the main chatbot script:

    python main.py

You will enter an interactive prompt:

- Ask questions about the loan approval dataset.
- Type `exit` or `quit` to end the session.

---

## How It Works

1. **Data Loading:** Reads and converts each row of the CSV dataset into a text chunk.
2. **Embedding:** Converts text chunks into vector embeddings.
3. **Vector Search:** Builds a FAISS index for fast similarity search.
4. **Retrieval:** For each user query, finds the most relevant chunks.
5. **Generation:** Passes the retrieved context with the question to a language model to generate an answer.

---

## Customization

- Replace the model in `generator.py` with any Hugging Face model or an API-based LLM (e.g., OpenAI GPT).
- Enhance data chunking or support other datasets.
- Integrate a web UI (Streamlit, Gradio) or an API server (FastAPI).
- Use a scalable vector store such as Pinecone, Chroma, or Weaviate for large-scale applications.

---

## License

This project is open for educational and research purposes. Modify and extend as needed.

---

## References

- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Kaggle Loan Approval Dataset](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction)

---

Feel free to open issues or request features!

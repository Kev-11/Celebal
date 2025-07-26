import pandas as pd
from embedder import Embedder
from vectorstore import VectorStore
from retriever import Retriever
from generator import Generator
from rag_chain import RAGChain

def load_and_chunk(csv_path):
    df = pd.read_csv(csv_path)
    # For each row, concatenate columns to text
    return df.astype(str).apply(lambda row: " ".join(row), axis=1).tolist()

if __name__ == "__main__":
    # 1. Load and chunk data
    docs = load_and_chunk('Training Dataset.csv')
    print(f"Loaded {len(docs)} rows.")

    # 2. Embedding
    embedder = Embedder()
    vectors = embedder.embed(docs)

    # 3. Vector DB
    vectorstore = VectorStore(vectors.shape[1])
    vectorstore.add(vectors, docs)

    # 4. Retriever & Generator
    retriever = Retriever(embedder, vectorstore)
    generator = Generator()  # You may specify device="cuda" if your GPU supports

    # 5. RAG chain orchestration
    rag = RAGChain(retriever, generator)

    # 6. REPL loop
    print("Loan RAG Q&A chatbot. Type 'exit' to quit.")
    while True:
        q = input("Ask: ")
        if q.lower() in {'exit', 'quit'}:
            break
        a = rag.answer(q)
        print("Answer:", a)

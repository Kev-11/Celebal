import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, vectors, texts):
        # vectors: np.array, texts: list of str
        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_vector, top_k=3):
        D, I = self.index.search(query_vector, top_k)
        return [self.texts[i] for i in I[0]]

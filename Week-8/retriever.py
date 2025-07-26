class Retriever:
    def __init__(self, embedder, vectorstore):
        self.embedder = embedder
        self.vectorstore = vectorstore

    def retrieve(self, query, top_k=3):
        query_vec = self.embedder.embed([query])
        return self.vectorstore.search(query_vec, top_k)

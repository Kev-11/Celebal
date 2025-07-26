class RAGChain:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def answer(self, question):
        contexts = self.retriever.retrieve(question)
        return self.generator.generate(question, contexts)

from transformers import pipeline

class Generator:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device='cpu'):
        self.pipe = pipeline("text-generation", model=model_name, max_new_tokens=256, device=device)

    def generate(self, question, contexts):
        context = "\n".join(contexts)
        prompt = (
            f"You are a helpful assistant. Use the following loan data context to answer the question.\n"
            f"{context}\n\n"
            f"Question: {question}\n"
            f"Answer:"
        )
        out = self.pipe(prompt)[0]['generated_text']
        # To extract the answer after 'Answer:' 
        return out.split("Answer:")[-1].strip()

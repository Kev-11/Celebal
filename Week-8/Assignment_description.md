# 📝 Assignment Description - Week 8

## 🎯 Task Overview

In Week 8 of my internship at **Celebal Tech**, I was assigned to build a **Retrieval-Augmented Generation (RAG) based Q&A chatbot**. The objective was to create an intelligent system that uses a combination of document retrieval and generative models to provide contextually accurate answers to user queries about loan approvals.

This project focuses on integrating traditional search (retrieval) with a generative language model to produce answers that are both relevant and natural.

---

## 📌 Task Objectives

Design and implement a **RAG-based Q&A chatbot** with the following capabilities:

### 1. **Data Preparation**
- Use the **Loan Approval Prediction dataset** from [Kaggle](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction?select=Training+Dataset.csv).
- Preprocess and clean the data to make it suitable for document indexing and querying.
- Convert structured rows or metadata into meaningful text chunks or documents.

### 2. **Document Embedding and Indexing**
- Use an embedding model (e.g., `sentence-transformers`, `MiniLM`, or a Hugging Face encoder) to convert documents into vector form.
- Store these embeddings in a **vector database** such as FAISS, ChromaDB, or any LangChain-compatible store.

### 3. **Retrieval Module**
- When a user asks a question, encode the query and retrieve relevant chunks from the vector store using similarity search.
- Ensure the retrieval step is efficient and returns relevant context from the dataset.

### 4. **Generative Module (LLM)**
- Use a lightweight LLM from Hugging Face (e.g., `mistralai/Mistral-7B-Instruct`, `phi-2`, or `openai/gpt-3.5`) to generate answers.
- Combine retrieved documents with the query and prompt the LLM to answer based on that context.
- Optionally use LangChain's `RetrievalQA` chain or similar abstraction.

### 5. **Frontend Interface (Optional)**
- Build a simple Streamlit or Gradio interface for users to:
  - Enter questions
  - View retrieved context and generated answers

### 6. **Model Flexibility**
- Allow model swapping via config or CLI:
  - Hugging Face (offline/local)
  - OpenAI / Gemini / Claude (if API key and credits available)

---

## 🗃 Deliverables

- Requirements.txt with all dependencies.
- Readme.md with setup instructions.
- Main.py script implementing the RAG chatbot.

---

> ✅ *This assignment demonstrates your ability to build intelligent AI applications by combining search with generation, using both structured data and LLMs.*

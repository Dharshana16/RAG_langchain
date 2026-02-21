<<<<<<< HEAD
# RAG-Based Document Chatbot (Local Implementation)

A fully local Retrieval-Augmented Generation (RAG) chatbot built using Hugging Face Transformers, Sentence Transformers, and Chroma Vector Database. The system performs semantic search over indexed documents and generates context-aware responses via a Transformer-based language model.

---

## Overview

This project implements a complete RAG pipeline:

1. Document ingestion and chunking  
2. Semantic embedding generation  
3. Vector storage using Chroma  
4. Top-k similarity retrieval  
5. Context-grounded answer generation using FLAN-T5  
6. Interactive Streamlit interface  

The system runs fully locally without external APIs.

---

## Architecture

```
Documents
→ Chunking
→ Embeddings (MiniLM)
→ Chroma Vector DB
→ Query Embedding
→ Similarity Search (Top-k + Threshold)
→ Context Construction
→ FLAN-T5 Generation
→ Streamlit UI
```

---

## Technologies Used

- Python  
- Hugging Face Transformers (FLAN-T5)  
- Sentence Transformers (MiniLM)  
- Chroma Vector Database  
- LangChain  
- Streamlit  

---

## Project Structure

```
rag_llm/
│
├── create_database.py      # Document ingestion and vector indexing
├── retrieval.py            # Semantic retrieval logic
├── llm_handler.py          # Transformer-based generation layer
├── query_data.py           # CLI-based querying
├── app.py                  # Streamlit UI
├── chroma/                 # Persisted vector database
└── data/books/             # Input documents
```

---

## Setup Instructions

### 1. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```
pip install sentence-transformers
pip install transformers
pip install langchain langchain-community chromadb
pip install streamlit
```

### 3. Build Vector Database

```
python create_database.py
```

### 4. Run Streamlit Application

```
python -m streamlit run app.py
```

---

## How It Works

### Document Processing
Documents inside `data/books/` are split into overlapping chunks to balance semantic precision and contextual completeness.

### Embeddings
Each chunk is converted into a dense vector using `all-MiniLM-L6-v2`.

### Vector Database
Embeddings are stored in Chroma for efficient similarity search and persistence.

### Retrieval
User queries are embedded and matched against stored vectors using cosine similarity with top-k retrieval and relevance score filtering.

### Generation
Retrieved context is injected into a structured prompt and passed to FLAN-T5 (encoder-decoder model) for grounded answer generation using the Transformers library.

---

## Design Decisions

- Fully local execution to avoid API dependency  
- Modular architecture separating ingestion, retrieval, and generation layers  
- CPU-compatible lightweight models for reproducibility  
- Prompt engineering to reduce hallucination and improve grounding  

---

## Potential Improvements

- Replace FLAN-T5 with LLaMA 3 or Mistral for stronger reasoning  
- Introduce hybrid retrieval (BM25 + embeddings)  
- Add re-ranking models  
- Implement conversational memory  
- Deploy as a scalable API service  

---

## Example Query

Query:
Who is Alice in the story?

Sample Generated Response:
Alice is a young girl who appears in the story.

---

## License

This project is for educational and research purposes.

---

## Author

Developed as a demonstration of Retrieval-Augmented Generation architecture using local Transformer models.
=======
# RAG_langchain
>>>>>>> bded7e997d12d7a0d8eee44c699e0d324c6fc31d

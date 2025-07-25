"# # 🧠 AI Lawyer Chatbot — RAG-Powered Legal Assistant

A powerful **GenAI reasoning chatbot** built using Retrieval-Augmented Generation (RAG) with **LangChain**, **DeepSeek**, **FAISS**, and **Streamlit**. This chatbot can answer legal queries based on user-uploaded documents like the *Universal Declaration of Human Rights* using deep reasoning and contextual understanding.

---

## 🚀 Features

- 🧾 Upload legal documents (PDFs)
- 🔍 Chunking + smart vector embedding
- 🧠 Uses DeepSeek-R1 via Ollama for embedding
- ⚡ Groq-hosted LLM (deepseek-r1-distill-llama-70b)
- 🧠 Accurate responses limited to the provided context
- 🖥️ Simple frontend via Streamlit

---

## 📦 Tech Stack

| Layer       | Technology |
|------------|-------------|
| Frontend   | Streamlit |
| Embedding  | DeepSeek R1 via Ollama |
| Vector DB  | FAISS |
| LLM Backend| Groq API |
| Framework  | LangChain |
| Language   | Python 3.10 |

---

## 🔧 Setup Instructions

### 1. Create Environment
```bash
conda create -n myenv python=3.10
conda activate myenv
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. API Keys & Models

* Add your **Groq API key** to environment variables:

  ```bash
  export GROQ_API_KEY="your_groq_key"
  ```
* Make sure **Ollama** is installed locally and the `deepseek-r1:1.5b` model is pulled.

---

## 🛠 Project Structure

```
.
├── frontend.py               # Streamlit frontend
├── vector_database.py       # Document loading, chunking, embedding, and FAISS setup
├── rag_pipeline.py          # LLM interaction, document retrieval, QA system
├── requirements.txt
└── README.md
```

---

## 📚 How It Works

### 🔹 Document Loading

PDFs are processed with `PDFPlumberLoader`, then chunked using `RecursiveCharacterTextSplitter`.

### 🔹 Embeddings

Embeddings are generated using the **DeepSeek R1** model locally via Ollama.

### 🔹 FAISS Indexing

All document chunks are embedded and stored in a local FAISS index.

### 🔹 RAG Pipeline

1. Query is embedded
2. Relevant document chunks are retrieved via FAISS
3. Context is built
4. A final prompt is sent to **Groq-hosted LLM**
5. Answer is generated based only on the retrieved context



## 🧠 Model Used

* Embeddings: `deepseek-r1:1.5b` via Ollama
* LLM: `deepseek-r1-distill-llama-70b` via Groq






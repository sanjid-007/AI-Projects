# 📄 RAG PDF Chatbot

A conversational AI app that lets you **upload any PDF and chat with it**. Ask questions, get context-aware answers, and have multi-turn conversations — all powered by Retrieval-Augmented Generation (RAG).

🚀 **Live Demo** → [ask-me-from-pdf.streamlit.app](https://ask-me-from-pdf.streamlit.app)

---

## ✨ Features

- 📂 Upload any PDF document
- 💬 Ask questions in natural language
- 🧠 Multi-turn conversation with memory
- ⚡ Fast responses powered by Groq LLM
- 🔍 Semantic search using sentence embeddings
- 🗄️ Vector storage with ChromaDB

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| LLM | Groq (LLaMA 3) |
| Embeddings | Sentence Transformers |
| Vector Store | ChromaDB |
| PDF Parsing | PyPDF |
| Language | Python 3.11 |

---

## 📁 Project Structure

```
rag-project/
├── app.py              # Streamlit UI and chat logic
├── ingest.py           # PDF loading, chunking, embedding
├── query.py            # Retrieval and answer generation
├── requirements.txt    # Project dependencies
├── .env                # API keys (not pushed to GitHub)
└── README.md
```

---

## ⚙️ How It Works

```
PDF Upload
    ↓
Split into chunks (ingest.py)
    ↓
Convert chunks to embeddings (Sentence Transformers)
    ↓
Store embeddings in ChromaDB
    ↓
User asks a question
    ↓
Find most relevant chunks (semantic search)
    ↓
Send chunks + question + chat history to Groq LLM
    ↓
Return answer to user
```

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/AI-Projects.git
cd AI-Projects/rag-project
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

**5. Run the app**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## ☁️ Deployment

This app is deployed on **Streamlit Community Cloud**.

To deploy your own instance:
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add `GROQ_API_KEY` in the Secrets section
5. Deploy

---

## 📌 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

---

## 📄 License

MIT License — feel free to use and modify.
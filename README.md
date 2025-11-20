# 🎬 Mini RAG System (Movie Plots)

A lightweight, modular Retrieval-Augmented Generation (RAG) system capable of answering natural language questions about movie plots. Built with **LangChain**, **NVIDIA NIM**, and **FAISS**.

![Architecture Diagram](https://your-image-link-here.com)
*(Replace the link above with your Excalidraw image link or keep it in the repo)*

## 🚀 Features
* **Modular Architecture:** Separated logic for ingestion (`preprocess.py`) and inference (`rag_engine.py`).
* **Persistent Storage:** Uses FAISS to store vector embeddings on disk, preventing expensive re-indexing.
* **Structured Output:** Guarantees valid JSON responses with citations and reasoning using Pydantic parsers.
* **Smart Chunking:** Uses `RecursiveCharacterTextSplitter` to preserve context in long movie plots.

---

## 📺 Video Walkthrough
**[▶️ Click Here to Watch the Demo Video](YOUR_LOOM_VIDEO_LINK_HERE)**

In this 2-minute video, I explain the end-to-end workflow:
1.  **Ingestion:** Loading and embedding 500+ movie plots.
2.  **Retrieval:** Performing semantic similarity search.
3.  **Generation:** Producing an evidence-based answer.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/arsath-eng/movie-rag.git](https://github.com/arsath-eng/movie-rag.git)
cd movie-rag

2. Setup EnvironmentIt is recommended to use a virtual environment:Bash# Create virtual environment
python -m venv venv5

# Activate it
# Windows:
venv5\Scripts\activate
# Mac/Linux:
source venv5/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. ConfigurationCreate a .env file in the root directory and add your NVIDIA API Key:PlaintextNVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
5. Download DataDownload wiki_movie_plots_deduped.csv from Kaggle.Place it in the data/ folder:Plaintextmovie_rag/data/wiki_movie_plots_deduped.csv
🏃‍♂️ UsageRun the main application via the command line:Bashpython -m app.main
What happens next:The app checks for an existing FAISS index in data/faiss_index/.If found: It loads instantly.If not found: It loads the CSV, chunks the text, generates embeddings (via NVIDIA), and saves the index for future use.You can then ask questions interactively.Example Query:"Describe the ending of The Great Train Robbery."Example JSON Output:JSON{
    "answer": "The bandits are eventually tracked down by a posse...",
    "contexts": ["The men quickly form a posse..."],
    "reasoning": "I found details about the shootout in the provided text."
}
🧠 Architecture FlowExcalidraw Diagram LinkThe system follows a strict RAG pipeline:Ingestion: Raw CSV $\rightarrow$ Cleaning $\rightarrow$ Chunking (300 words) $\rightarrow$ NVIDIA Embeddings $\rightarrow$ FAISS Vector Store.Retrieval: User Query $\rightarrow$ Embedding $\rightarrow$ Similarity Search (Top-3).Generation: Context + Query $\rightarrow$ Llama-3-70b (NVIDIA NIM) $\rightarrow$ JSON Parser.📂 Project StructurePlaintextmovie_rag/
├── app/
│   ├── main.py             # Entry point
│   ├── preprocess.py       # Data cleaning & chunking
│   ├── rag_engine.py       # Class for NVIDIA & FAISS logic
│   └── __init__.py
├── data/
│   ├── faiss_index/        # Generated locally (Gitignored)
│   └── wiki_movie...csv    # Dataset (Gitignored)
├── notebooks/
│   └── exploration.ipynb   # Data analysis & prototyping
├── requirements.txt
└── README.md

### **Final Action List for You:**
1.  **Create `.gitignore`** with the code above.
2.  **Create `README.md`** with the code above.
3.  **Paste your Links:** Open `README.md` and replace `YOUR_LOOM_VIDEO_LINK_HERE` and `YOUR_EXCALIDRAW_LINK_HERE` with your actual links.
4.  **Commit & Push:**
    ```bash
    git add .
    git commit -m "Final submission: Mini RAG System with modular architecture"
    git push origin main
    ```


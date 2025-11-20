# 🎬 Mini RAG System (Movie Plots)

A lightweight, modular **Retrieval-Augmented Generation (RAG)** system designed to answer questions about movie plots with high accuracy. Built using **LangChain**, **NVIDIA NIM** (Llama 3), and **FAISS** for vector storage.

# Architecture Diagram
<img width="1788" height="1371" alt="Snapdrumpng" src="https://github.com/user-attachments/assets/448f9d3a-785e-4e3c-8504-23f0d08ac15e" />



## ✨ Key Features
- Persistent FAISS index → loads in **<2 seconds** after first run
- Structured JSON answers with sources & reasoning
- Smart chunking (300 tokens) that keeps plot spoilers intact
- Completely **free for 6+ months** using NVIDIA's generous trial
- No OpenAI costs, no rate-limit headaches

---

## 📺 Video Demo

Click the image below to watch the walkthrough:

[![Watch Video](https://img.shields.io/badge/Watch%20Video-Loom-blue?style=for-the-badge&logo=loom)](https://www.loom.com/share/a1631ffffcd644b1bdb18681d0f9f0c3)

---

## 🚀 Quick Start (5 Minutes)

### 1. Clone the Repo
```bash
git clone https://github.com/arsath-eng/Snapdrum-Assignment.git
cd Snapdrum-Assignment
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Your Free NVIDIA API Key (Valid for 6 Months)
→ Go to: https://build.nvidia.com  
→ Sign in with Google/GitHub  
→ Choose "NVIDIA NIM" → "Llama 3 70B Instruct" or "meta/llama3-70b-instruct"  
→ Click "Get API Key" → Copy the key (starts with `nvapi-...`)  
→ It's completely free for the first 6 months with generous rate limits!

### 5. Create `.env` File
```bash
echo "NVIDIA_API_KEY=nvapi-your-key-here" > .env
```

### 6. Download the Dataset
1. Go to: https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots
2. Download `wiki_movie_plots_deduped.csv`
3. Place it in the `data/` folder:
```
movie-rag/data/wiki_movie_plots_deduped.csv
```

---

## ▶️ Run the App

```bash
python -m app.main
```

What happens:
- First run → embeds all 30k+ movie plots (~3–5 min with NVIDIA NIM)
- Saves FAISS index locally → next runs are instant (<2 sec load)
- Then enters interactive mode

### Example Queries and Response
<img width="1122" height="286" alt="image" src="https://github.com/user-attachments/assets/b05fcc37-b2c4-4e3f-b687-3c241e29c2ad" />

<img width="1109" height="461" alt="image" src="https://github.com/user-attachments/assets/0ddfa819-b35f-4909-b1f1-2fa1907017a5" />

---

## 🧠 Architecture Flow


Full Excalidraw (editable): [Workflow
](https://excalidraw.com/#json=LPkG0cm-JxBwfObZdItwH,X4DpsxcGldb4scbiMWT_1g)
---

## 📂 Project Structure
```
movie-rag/
├── app/
│   ├── main.py             # CLI entry point
│   ├── preprocess.py       # Cleaning & chunking
│   ├── rag_engine.py       # FAISS + NVIDIA logic
│   └── __init__.py
├── data/
│   ├── faiss_index/        # Auto-generated (gitignored)
│   └── wiki_movie_plots_deduped.csv
├── notebooks/
│   └── exploration.ipynb
├── requirements.txt
└── README.md
```





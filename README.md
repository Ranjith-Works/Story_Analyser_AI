# 🔍 Story Detective AI

AI-powered story analysis using **Retrieval-Augmented Generation (RAG)**.

Upload a story (PDF / TXT / DOCX) and explore it through six lenses: ask questions, investigate characters, build a timeline, summarize, review quality, and rewrite the ending.

> Generative AI Capstone Project — LevelShift AIML Training (Day 30).

## Features

- 💬 **Ask the Story** — question answering grounded in the uploaded text
- 🕵 **Character Detective** — character extraction and analysis
- 📜 **Story Timeline** — chronological event reconstruction
- 📚 **Story Summary** — concise summaries
- 🎯 **Story Review** — quality/craft feedback
- ✨ **Rewrite the Ending** — generate alternate endings

## Tech Stack

- **Streamlit** — UI
- **OpenRouter API** — LLM inference
- **Sentence Transformers** — embeddings
- **FAISS** — vector store
- **RAG** — retrieval-augmented generation

## Setup

```bash
# 1. Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env         # then add your OpenRouter API key
```

Set your key in `.env`:

```
OPENROUTER_API_KEY=your_key_here
```

## Run

```bash
streamlit run app.py
```

## Project Structure

```
├── app.py                 # Streamlit entry point
├── backend/               # Core logic
│   ├── story_processor.py # File → chunks → index pipeline
│   ├── embeddings.py      # Sentence-transformer embeddings
│   ├── rag.py             # Retrieval + generation
│   ├── llm.py             # OpenRouter LLM client
│   ├── prompts.py         # Prompt templates
│   ├── file_loader.py     # PDF/TXT/DOCX loaders
│   └── utils.py
└── views/                 # Streamlit page modules
    ├── chat.py  character.py  timeline.py
    ├── summary.py  quality.py  ending.py
```
## I am doing this edit to check whetehr Jenkins is able to identify my changes

sample check on 8 Jul 26jjjjjjjjjjjjjjj

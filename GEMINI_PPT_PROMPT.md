# Gemini Prompt — Generate Capstone Presentation

Copy everything inside the box below and paste it into Gemini.

---

You are an expert presentation designer and technical writer. Create a **detailed, professional, academic-grade PowerPoint presentation** for a **Generative AI Capstone Project assignment submission**. The presentation must be suitable for evaluation by a technical instructor and should demonstrate a strong, clear understanding of Generative AI, RAG (Retrieval-Augmented Generation), and software engineering.

Produce the output as a **complete slide-by-slide deck**. For **each slide**, give me:
1. **Slide title**
2. **Body content** (bullet points, kept concise and presentation-ready — not paragraphs)
3. **Visual suggestion** (diagram, icon, chart, or layout idea)

### IMPORTANT RULES
- **DO NOT include speaker notes** on any slide.
- **Use simple, plain English.** Avoid hard, fancy, or overly technical jargon. If a technical term must be used (like "embedding" or "vector"), explain it in a few simple words. A reader who is new to AI should easily understand every slide.
- **Do NOT use external stock images** and **do NOT add an "Image Sources" slide.** Use only simple icons, diagrams, and layouts.
- Keep phrasing short and easy to read.

## PROJECT DETAILS (use these exact facts — do not invent features)

**Project name:** Story Detective AI
**Tagline:** AI-powered Story Analysis using Retrieval-Augmented Generation (RAG)
**Type:** Generative AI Capstone Project
**Category:** RAG-based document intelligence application

### What it does
A user uploads a story document (PDF, TXT, or DOCX). The app reads it and turns it into a searchable knowledge base, then offers six AI-powered features to analyze the story. All AI answers are based strictly on the uploaded story (so the model does not make things up).

### Technology stack
- **Frontend / UI:** Streamlit (wide layout, sidebar navigation, custom CSS)
- **LLM (the AI model):** OpenRouter API, model `nvidia/nemotron-3-ultra-550b-a55b:free`, used through the OpenAI Python SDK
- **Embeddings (turning text into numbers):** Sentence Transformers, model `all-MiniLM-L6-v2`
- **Vector store (the search database):** FAISS (`IndexFlatL2` — L2 / straight-line distance)
- **Document reading:** pypdf (PDF), python-docx (DOCX), plain decode (TXT)
- **Config / secrets:** python-dotenv (`.env` holds `OPENROUTER_API_KEY`)
- **Core libs:** numpy
- **Language:** Python 3.12

### Architecture (organized, modular design)
- `app.py` — the main Streamlit file: page setup, saved app state, file upload, metrics, and sidebar menu
- **`backend/` folder (the logic):**
  - `story_processor.py` — runs the full story-processing steps in order
  - `file_loader.py` — reads the text out of PDF/TXT/DOCX files
  - `utils.py` — `chunk_text()` splits the text into small overlapping pieces
  - `embeddings.py` — loads the model and turns text pieces into numbers
  - `rag.py` — builds the search database and finds the most relevant pieces
  - `llm.py` — talks to the AI model, gets answers, and finds character names
  - `prompts.py` — all the instruction templates for the AI (chat, character, timeline, summary, quality, ending)
- **`views/` folder (the screens):** `chat.py`, `character.py`, `timeline.py`, `summary.py`, `quality.py`, `ending.py`
- The design keeps the screens (views) separate from the logic (backend), which keeps the code clean and easy to change.

### How it works (step by step)
1. **Upload** — the user uploads a PDF/TXT/DOCX file
2. **Read** — the app pulls out the plain text based on the file type
3. **Split** — the text is split into pieces of **500 characters** with a **100-character overlap** (the overlap keeps the meaning connected between pieces)
4. **Convert** — each piece is turned into a list of numbers (an "embedding") using the `all-MiniLM-L6-v2` model
5. **Store** — those numbers are saved in a FAISS search database
6. **Find characters** — the AI reads the first ~12,000 characters and returns a clean, sorted list of character names
7. **Search (when a question is asked)** — the question is turned into numbers, and FAISS finds the closest matching pieces (top-3 for chat, top-5 for character analysis)
8. **Answer** — those matching pieces are given to the AI along with the question, and the AI answers using only that information

### The six features
1. **Ask the Story (Chat)** — ask any question; the app finds the top-3 matching pieces and answers only from the story. If the answer isn't in the story, it says so. It also shows the exact pieces it used, so the user can check.
2. **Character Detective** — pick a character from the auto-found list; the app finds the top-5 matching pieces and gives a clear profile (Role, Personality, Relationships, Major Events, Character Arc, Interesting Facts)
3. **Story Timeline** — creates a list of the main events in order
4. **Story Summary** — writes a short summary of the story
5. **Story Review (Quality Analysis)** — acts like a story reviewer; gives a score out of 10 for Plot, Character Development, World Building, Pacing, Dialogue, and Ending, plus strengths, weaknesses, and a final verdict
6. **Rewrite the Ending** — writes a new ~400-word ending that keeps the same characters and writing style

### Key design choices to highlight (in simple terms)
- **No made-up answers:** the AI is told to answer only from the story pieces and to say when the answer isn't there
- **Overlapping pieces:** the 100-character overlap stops the meaning from being cut off between pieces
- **Clean structure:** the logic is kept separate from the screens, so the app is easy to test and grow
- **Saved app state:** the processed story, pieces, database, and characters are kept in memory so the app doesn't redo the work every time
- **Free/low-cost tools:** the text-to-numbers step runs locally (no cost) and the AI model uses a free tier

### Limitations & honest evaluation (include a slide — instructors like honesty)
- Finding character names depends on the AI and is not always perfect
- The timeline, summary, quality, and ending features use only the first ~25–30 pieces, so very long stories may not be fully covered
- The FAISS search checks every item one by one, so it would slow down for very large collections
- Nothing is saved to disk — the search database is rebuilt every session; there is no database
- It is a single-user local app; there is no login or multi-user support

### Possible future improvements (include a slide)
- Save the search database to disk (for example with Chroma or pgvector) so it isn't rebuilt each time
- Split text by sentences/meaning instead of a fixed 500-character size
- Cover the whole document (not just the start) by summarizing in parts and combining
- Support multiple stories and compare them
- Add live streaming answers and chat memory
- Deploy online (Streamlit Cloud / Docker) and add a login

## REQUIRED SLIDE STRUCTURE (follow this order, ~15 slides)

1. **Title slide** — project name, tagline, and "Generative AI Capstone Project". Put the name **Ranjith Balu** directly under the title. Do NOT add "Capstone Student", "Submission Category", or "Evaluated By".
2. **Agenda / What we'll cover**
3. **Problem Statement** — why reading and analyzing long stories by hand is hard, and why a plain AI alone isn't enough
4. **Project Overview** — what Story Detective AI is, in one clear picture
5. **What is RAG?** — a simple explanation (find the right text, add it to the question, then let the AI answer) and why it's better than a plain AI for questions about a document
6. **Technology Stack** — grouped by part (UI, text-to-numbers, search database, AI model, file reading) with a short, simple "why we chose it" for each
7. **System Architecture** — a diagram of app.py ↔ backend ↔ views; explain how the screens and the logic are kept separate
8. **How It Works — Processing the Story** — upload → read → split → convert → store (with a simple flow diagram)
9. **How It Works — Answering a Question** — question → convert → find closest pieces → add to prompt → AI answers (with a simple flow diagram)
10. **Feature 1 — Ask the Story (Chat)**
11. **Feature 2 — Character Detective**
12. **Features 3 & 4 — Timeline & Summary** (share one slide)
13. **Features 5 & 6 — Story Review & Rewrite the Ending** (share one slide)
14. **Limitations & Honest Evaluation**
15. **Future Improvements**

Do NOT add a "Conclusion & Q&A" slide and do NOT add an "Image Sources" slide.

## DESIGN & FORMATTING REQUIREMENTS
- Clean, modern, professional academic look; suggest one simple color palette (the app uses a blue accent `#4F8BF9` on a dark background — match that)
- Consistent fonts and layout; readable font sizes
- Prefer simple diagrams and flowcharts over long text (especially for the architecture slide and the two "how it works" slides — describe them clearly enough that they can be drawn easily)
- Use simple icons where helpful
- Every slide: max ~6 bullets, short and clear phrasing
- Remember: no speaker notes, no external images, plain and easy language throughout
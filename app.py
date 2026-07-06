import streamlit as st

from backend.story_processor import process_story

from views.chat import show_chat
from views.character import show_character
from views.timeline import show_timeline
from views.summary import show_summary
from views.quality import show_quality
from views.ending import show_ending


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Story Detective AI",
    page_icon="🔍",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    padding-top: 1rem;
}

/* Header */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    background: linear-gradient(90deg, #4F8BF9 0%, #6FD3FF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    color: #9AA4B2;
    font-size: 18px;
    margin-bottom: 20px;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(79,139,249,0.10), rgba(79,139,249,0.02));
    border: 1px solid rgba(79,139,249,0.25);
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(79,139,249,0.25);
}

[data-testid="stMetricValue"] {
    font-weight: 700;
    color: #4F8BF9;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #4F8BF9 0%, #3A6FD8 100%);
    color: #fff;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
    transition: all 0.15s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(79,139,249,0.4);
    color: #fff;
}

/* Headers inside pages */
h1, h2, h3 {
    font-weight: 700 !important;
    letter-spacing: -0.3px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(79,139,249,0.06), rgba(0,0,0,0));
}

/* Expander polish */
[data-testid="stExpander"] {
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* File uploader */
[data-testid="stFileUploader"] {
    border: 1.5px dashed rgba(79,139,249,0.4);
    border-radius: 14px;
    padding: 12px;
    background: rgba(79,139,249,0.03);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("""
<div class="main-title">
🔍 Story Detective AI
</div>

<div class="subtitle">
AI-powered Story Analysis using Retrieval-Augmented Generation (RAG)
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

defaults = {
    "story": None,
    "chunks": None,
    "index": None,
    "characters": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------------

st.subheader("📄 Upload Story")

uploaded_file = st.file_uploader(
    "Upload",
    type=["pdf", "txt", "docx"],
    label_visibility="collapsed"
)

if uploaded_file and st.session_state.story is None:

    with st.spinner("Processing story..."):

        story_data = process_story(uploaded_file)

        st.session_state.update(story_data)

# ---------------------------------------------------------
# MAIN APP
# ---------------------------------------------------------

if st.session_state.story:

    st.success("✅ Story processed successfully!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👥 Characters",
            len(st.session_state.characters)
        )

    with col2:
        st.metric(
            "📑 Chunks",
            len(st.session_state.chunks)
        )

    with col3:
        st.metric(
            "📝 Words",
            f"{len(st.session_state.story.split()):,}"
        )

    st.divider()

    with st.expander("📖 Story Preview"):

        st.text_area(
            "",
            st.session_state.story[:3000],
            height=250
        )

    st.divider()

    page = st.sidebar.radio(

        "🧭 Navigation",

        [

            "💬 Ask the Story",

            "🕵 Character Detective",

            "📜 Story Timeline",

            "📚 Story Summary",

            "🎯 Story Review",

            "✨ Rewrite the Ending"

        ]

    )

    if page == "💬 Ask the Story":

        show_chat()

    elif page == "🕵 Character Detective":

        show_character()

    elif page == "📜 Story Timeline":

        show_timeline()

    elif page == "📚 Story Summary":

        show_summary()

    elif page == "🎯 Story Review":

        show_quality()

    elif page == "✨ Rewrite the Ending":

        show_ending()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.divider()

st.sidebar.metric(
    "Characters Found",
    len(st.session_state.characters)
)

st.sidebar.metric(
    "Story Chunks",
    len(st.session_state.chunks or [])
)

st.sidebar.divider()

if st.sidebar.button("🔄 Upload New Story"):

    for key in defaults:
        st.session_state[key] = defaults[key]

    st.rerun()

st.sidebar.divider()

st.sidebar.markdown("### 🚀 Tech Stack")

st.sidebar.write("• Streamlit")
st.sidebar.write("• OpenRouter API")
st.sidebar.write("• Sentence Transformers")
st.sidebar.write("• FAISS Vector Store")
st.sidebar.write("• Retrieval-Augmented Generation")

st.sidebar.divider()

st.sidebar.caption("Generative AI Capstone Project")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "🔍 Story Detective AI | Built using Streamlit • FAISS • Sentence Transformers • OpenRouter"
)
import streamlit as st

from backend.embeddings import model
from backend.rag import retrieve_chunks
from backend.llm import generate_response
from backend.prompts import CHARACTER_PROMPT


def show_character():

    st.header("👤 Character Detective")

    character = st.selectbox(
        "Choose Character",
        st.session_state.characters,
        key="character_select"
    )

    if st.button("Analyze Character", key="character_button"):

        retrieved = retrieve_chunks(
            character,
            model,
            st.session_state.index,
            st.session_state.chunks,
            k=5
        )

        context = "\n\n".join(retrieved)

        prompt = CHARACTER_PROMPT.format(
            context=context,
            question=character
        )

        answer = generate_response(prompt)

        st.markdown(answer)
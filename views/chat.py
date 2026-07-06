import streamlit as st

from backend.embeddings import model
from backend.rag import retrieve_chunks
from backend.llm import ask_llm


def show_chat():

    st.header("💬 Story Chat")

    question = st.text_input(
        "Ask a question about the story",
        key="chat_question"
    )

    if st.button("Ask AI", key="chat_button"):

        retrieved = retrieve_chunks(
            question,
            model,
            st.session_state.index,
            st.session_state.chunks
        )

        context = "\n\n".join(retrieved)

        answer = ask_llm(
            context,
            question
        )

        st.markdown(answer)

        with st.expander("Retrieved Context"):
            st.write(context)
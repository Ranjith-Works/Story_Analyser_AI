import streamlit as st

from backend.prompts import TIMELINE_PROMPT
from backend.llm import generate_response


def show_timeline():

    st.header("📅 Timeline Generator")

    if st.button(
        "Generate Timeline",
        key="timeline_button"
    ):

        context = "\n\n".join(
            st.session_state.chunks[:25]
        )

        prompt = TIMELINE_PROMPT.format(
            context=context
        )

        answer = generate_response(prompt)

        st.markdown(answer)
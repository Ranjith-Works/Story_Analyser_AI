import streamlit as st

from backend.prompts import QUALITY_PROMPT
from backend.llm import generate_response


def show_quality():

    st.header("⭐ Story Quality Analysis")

    if st.button("Analyze Story Quality"):

        with st.spinner("Reviewing Story..."):

            context = "\n\n".join(
                st.session_state.chunks[:30]
            )

            prompt = QUALITY_PROMPT.format(
                context=context
            )

            answer = generate_response(prompt)

            st.markdown(answer)
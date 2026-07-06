import streamlit as st

from backend.prompts import SUMMARY_PROMPT
from backend.llm import generate_response


def show_summary():

    st.header("📝 Story Summary")

    st.write("Generate an AI summary of the uploaded story.")

    if st.button("Generate Summary"):

        with st.spinner("Summarizing Story..."):

            context = "\n\n".join(
                st.session_state.chunks[:30]
            )

            prompt = SUMMARY_PROMPT.format(
                context=context
            )

            answer = generate_response(prompt)

            st.markdown(answer)
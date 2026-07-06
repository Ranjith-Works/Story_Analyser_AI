import streamlit as st

from backend.prompts import ENDING_PROMPT
from backend.llm import generate_response


def show_ending():

    st.header("🎭 Alternate Ending Generator")

    if st.button("Generate Alternate Ending"):

        with st.spinner("Writing Alternate Ending..."):

            context = "\n\n".join(
                st.session_state.chunks[:30]
            )

            prompt = ENDING_PROMPT.format(
                context=context
            )

            answer = generate_response(prompt)

            st.markdown(answer)
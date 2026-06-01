import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend.llm_service import translate_and_explain

def show():
    st.header("Learn Kannada")

    user_input = st.text_input("Enter English sentence")

    if st.button("Translate"):
        if user_input:
            with st.spinner("Thinking..."):
                result = translate_and_explain(user_input)
                st.success(result)

show()
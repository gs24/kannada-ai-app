import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend.llm_service import correct_sentence

def show():
    st.header("Practice Kannada")

    user_input = st.text_input('Write in Kannada (or type in English like: "naanu hogtini")')

    if st.button("Check"):
        if user_input:
            with st.spinner("Checking..."):
                result = correct_sentence(user_input)
                st.success(result)


show()
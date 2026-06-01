import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.pages import learn, practice, quiz

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.llm_service import translate_and_explain, correct_sentence

st.set_page_config(page_title="Kannada AI App", page_icon=":books:", layout="centered")

st.title("Kannada Learning App")

menu  =["Learn words", "Practice"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Learn words":
    learn.show()
elif choice == "Practice":
    practice.show()               
elif choice == "Quiz":
    quiz.show()   
import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from backend.quiz_engine import get_random_question

def show():
    st.header("Kannada Quiz")


    if "question" not in st.session_state:
        st.session_state.question = get_random_question()

    q =  st.session_state.question

    st.write(q['question'])

    selected_option = st.radio("Choose Answer", q['options'])

    if st.button("Submit"):
        if selected_option == q['correct']:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {q['correct']}")

    if st.button("Next Question"):
        st.session_state.question = get_random_question()


show()
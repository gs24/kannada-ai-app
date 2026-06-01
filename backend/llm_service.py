from groq import Groq
from dotenv import load_dotenv

import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def translate_and_explain(text):
    prompt = f"""
        You are a Kannada teacher for school kids.

        Tasks:
        1. Translate the sentence to Kannada.
        2. Explain the meaning in simple english
        3. Give one similar example
        4. Give the meaning of the sentence in English
        5. Give the kannada sentence in English letters (like: "naanu hogtini")

        Input: {text}
"""
    
    response = client.chat.completions.create(
        model = os.getenv("MODEL_TO_USE"),
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def correct_sentence(text):
    prompt = f"""
        You are a Kannada teacher for school kids.

        Tasks:
        1. Correct the sentence
        2. Explain mistakes in simple english
        3. Give correct Kannada sentence
        4. Give the kannada sentence in English letters (like: "naanu hogtini")
        5. Give the meaning of the sentence in English

        Input: {text}
"""
    
    response = client.chat.completions.create(
        model = os.getenv("MODEL_TO_USE"),
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
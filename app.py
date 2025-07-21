import streamlit as st
import pandas as pd
from fuzzywuzzy import process

# Load the Q&A data
df = pd.read_csv("eco_qa.csv")
questions = df['question'].tolist()
answers = df['answer'].tolist()

def get_response(user_input):
    match, score = process.extractOne(user_input, questions)
    if score > 60:
        return answers[questions.index(match)]
    else:
        return "🤖 Sorry, I don't have an answer yet. Try rephrasing your question."

# Streamlit UI
st.set_page_config(page_title="EcoAdvisor", page_icon="🌱")
st.title("🌱 EcoAdvisor - Your Eco-Friendly Assistant")
st.write("Ask anything about recycling, sustainability, waste reduction, or eco-friendly products.")

user_input = st.text_input("🗣️ Ask your question:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = get_response(user_input)
        st.markdown(f"**EcoAdvisor:** {response}")

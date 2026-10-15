from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

st.header("Reserching Tool")
model = ChatGroq(model="qwen/qwen3.8-27b")

user_input = st.text_input("Enter your text to summarise")

if st.button("Summerize"):
    if user_input:
        result=model.invoke(user_input)
        st.write(result.content)

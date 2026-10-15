# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# st.header("researching Tool")

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     max_new_tokens=256
# )

# model = ChatHuggingFace(llm=llm)

# user_input=st.text_input("Enter your Prompt")

# if st.button:
#     result=model.invoke(user_input)
#     st.write(result.content)



# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# model = ChatOpenAI(model="gpt-5.4-mini")

# user_input = st.text_input("Enter your text to summarise")


# st.header("Researching Tool")

# if st.button("Summerise"):
#     result=model.invoke(user_input)
#     st.write(result.content)



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
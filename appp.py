import streamlit as st
import google.generativeai as genai

st.title("welcome to my gemini chat")


genai.configure(api_key="AIzaSyAmLEMLPMNCJB5iYkYSStjS8RmCrT_Zwqo")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("click me"):
        response = chat.send_message(text)
        st.write(response.text)
        
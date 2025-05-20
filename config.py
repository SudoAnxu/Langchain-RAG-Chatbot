import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
LLM_MODEL = "llama-3.1-8b-instant"
CHROMA_DIR = "./chroma_db"
DATA_FILE = "data.txt"

from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import retrieval_qa
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import streamlit as st

from wxai_langchain.llm import LangChainInterface

st.title("Ask WatsonX AI")

if 'messages' not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Ask me anything")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
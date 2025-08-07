import streamlit as st
from data_processing import load_and_create_documents
from vector_db import create_vector_database
from rag import create_rag_chain
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

RAW_DATA_FILE = os.getenv("RAW_DATA_FILE")

def initialize_chatbot():
    if 'qa_chain' not in st.session_state:
        with st.spinner('Loading....'):
            documents = load_and_create_documents(RAW_DATA_FILE)
            if not documents:
                st.error(f"ไม่สามารถโหลดข้อมูลได้ กรุณาตรวจสอบว่ามีไฟล์ '{RAW_DATA_FILE}' อยู่หรือไม่")
                return False

            vector_db = create_vector_database(documents)
            
            st.session_state.qa_chain = create_rag_chain(vector_db)
            
            st.session_state.messages = []
    return True

# --- Page Streamlit ---
st.set_page_config(page_title="Medical Chatbot", page_icon="🏥")
st.title("แชทบอทให้คำปรึกษาด้านการแพทย์")

if not initialize_chatbot():
    st.stop()

# --- Chat ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("พิมพ์คำถามของคุณที่นี่..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("กำลังค้นหาคำตอบ..."):
            response = st.session_state.qa_chain.invoke({"query": prompt})
            answer = response.get('result', 'ขออภัยค่ะ ไม่สามารถหาคำตอบได้')
            st.markdown(answer)
            
    st.session_state.messages.append({"role": "assistant", "content": answer})
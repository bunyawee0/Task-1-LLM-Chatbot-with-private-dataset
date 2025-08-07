from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME")

def create_vector_database(chunks):
    if not EMBEDDING_MODEL_NAME:
        raise ValueError("EMBEDDING_MODEL_NAME is not ")

    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'} 
    )
    
    
    print("กำลังสร้าง Vector Database...")
    vector_db = FAISS.from_documents(documents=chunks, embedding=embedding_model)
    print("Vector Database สร้างเสร็จสิ้น!")
    return vector_db
import pandas as pd
from langchain.schema.document import Document

def load_and_create_documents(file_path: str) -> list[Document]:
    """
    อ่านไฟล์ CSV, จัดรูปแบบข้อความ, และแปลงเป็น List ของ LangChain Document
    ฟังก์ชันนี้จะทำทุกอย่างให้เสร็จในที่เดียว
    """
    try:
        df = pd.read_csv(file_path)
        if 'question' not in df.columns or 'answer' not in df.columns:
            raise KeyError("ไฟล์ CSV ต้องมีคอลัมน์ 'question' และ 'answer'")

        documents = []
        for _, row in df.iterrows():
            if pd.notna(row['question']) and pd.notna(row['answer']):
                content = f"คำถาม: {row['question']}\nคำตอบ: {row['answer']}"
                documents.append(Document(page_content=content))
        
        print(f"เตรียมข้อมูลสำเร็จ {len(documents)} documents จากไฟล์ {file_path}")
        return documents

    except FileNotFoundError:
        print(f"Error: ไม่พบไฟล์ข้อมูล {file_path}")
        return []
    except KeyError as e:
        print(f"Error: {e}")
        return []
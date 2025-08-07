from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama 


def create_rag_chain(vector_db):
    llm = Ollama(model="mistral")
    
    prompt_template = """
    คุณคือผู้ช่วย AI ด้านสุขภาพที่ให้ข้อมูลอย่างเป็นมิตรและถูกต้อง
    จงใช้ "บริบท" ที่เป็นตัวอย่างคู่คำถามและคำตอบที่เกี่ยวข้อง เพื่อตอบ "คำถามจากผู้ใช้"
    พยายามตอบให้กระชับและตรงประเด็นที่สุด

    บริบท:
    {context}

    คำถามจากผู้ใช้: {question}

    คำตอบที่เป็นประโยชน์:
    """

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": PROMPT}
    )

    return qa_chain
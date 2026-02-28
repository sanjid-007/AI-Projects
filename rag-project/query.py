import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq
load_dotenv() 


model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("documents")


groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def find_relevant_chunks(question, n_results=3):
    question_embedding = model.encode([question]).tolist()
    
    results = collection.query(
        query_embeddings=question_embedding,
        n_results=n_results
    )
    
    return results['documents'][0]

def answer_question(question, chat_history=[]):
    relevant_chunks = find_relevant_chunks(question)
    context = "\n\n".join(relevant_chunks)
    system_prompt = f"""You are a document assistant. Answer ONLY using the context below.
Do NOT use outside knowledge. If the answer isn't in the context, say "I couldn't find that in the document."

DOCUMENT CONTEXT:
{context}"""
    messages = [{"role": "system", "content": system_prompt}]
    messages += chat_history 
    messages.append({"role": "user", "content": question}) 
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=1024
    )
    
    answer = response.choices[0].message.content
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "assistant", "content": answer})
    
    return answer, chat_history



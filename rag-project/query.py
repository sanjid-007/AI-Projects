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
    """Find the most relevant parts of the document for the question"""
    question_embedding = model.encode([question]).tolist()
    
    results = collection.query(
        query_embeddings=question_embedding,
        n_results=n_results
    )
    
    return results['documents'][0]

def answer_question(question):
    """Get an answer from Claude using relevant document chunks"""
  
    relevant_chunks = find_relevant_chunks(question)
    
    print("=== CHUNKS FOUND ===")
    for i, chunk in enumerate(relevant_chunks):
        print(f"Chunk {i+1}: {chunk[:200]}...")  # Print first 200 chars
    print("====================")
    context = "\n\n".join(relevant_chunks)
    
   
    prompt = f"""You are a document assistant. You MUST answer ONLY using the context below.
Do NOT use any outside knowledge. Do NOT guess.
If the answer is not explicitly in the context, say exactly: "I couldn't find that in the document."

CONTEXT FROM DOCUMENT:
{context}

QUESTION: {question}

ANSWER (based strictly on the context above):"""
    
    response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile", 
    messages=[{"role": "user", "content": prompt}],
    max_tokens=1024
)
    return response.choices[0].message.content



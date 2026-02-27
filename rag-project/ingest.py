from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("documents")

def read_pdf(file_path):
    """Read all text from a PDF file"""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_into_chunks(text, chunk_size=500):
    """Split text into smaller pieces so AI can process them"""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        current_chunk.append(word)
        current_size += 1
        if current_size >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_size = 0
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

def ingest_pdf(file_path):
    """Main function - read PDF, embed chunks, store in ChromaDB"""
    print("Reading PDF...")
    text = read_pdf(file_path)
    
    print("Splitting into chunks...")
    chunks = split_into_chunks(text)
    
    print(f"Creating embeddings for {len(chunks)} chunks...")
    embeddings = model.encode(chunks).tolist()
    
    print("Storing in ChromaDB...")
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    
    print(f"Done! Stored {len(chunks)} chunks from your PDF.")


if __name__ == "__main__":
    ingest_pdf("your_document.pdf")
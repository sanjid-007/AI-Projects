
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("documents")
print(f"Total chunks stored: {collection.count()}")
sample = collection.peek(1)
print(f"Sample chunk: {sample['documents'][0][:300]}")
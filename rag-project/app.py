import streamlit as st
import tempfile
import os

from ingest import ingest_pdf
from query import answer_question
st.title("📄 Chat with Your Document")
st.write("Upload a PDF and ask questions about it!")
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    
    if st.button("Process Document"):
        with st.spinner("Reading and storing your document..."):
            ingest_pdf(tmp_path)
        st.success("Document processed! You can now ask questions.")
        os.unlink(tmp_path)
st.divider()

st.subheader("Ask a Question")
question = st.text_input("Your question:")

if st.button("Get Answer") and question:
    with st.spinner("Searching document and generating answer..."):
        answer = answer_question(question)
    
    st.subheader("Answer:")
    st.write(answer)
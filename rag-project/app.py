import streamlit as st
import tempfile
import os
from ingest import ingest_pdf
from query import answer_question

st.title(" Chat with Your Document")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "messages_display" not in st.session_state:
    st.session_state.messages_display = []


with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
    
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
            
        with st.spinner("Processing..."):
            ingest_pdf(tmp_path)
            
        st.success("Document ready!")
        os.unlink(tmp_path)
    
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.messages_display = []
        st.rerun()


for msg in st.session_state.messages_display:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


question = st.chat_input("Ask a question about your document...")

if question:

    with st.chat_message("user"):
        st.write(question)
    

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, updated_history = answer_question(
                question, 
                st.session_state.chat_history
            )
        st.write(answer)
    

    st.session_state.chat_history = updated_history
    st.session_state.messages_display.append({"role": "user", "content": question})
    st.session_state.messages_display.append({"role": "assistant", "content": answer})
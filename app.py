import streamlit as st
from retrieval import retrieve_context
from llm_handler import generate_answer

st.title("📚 RAG Document Chatbot")

query = st.text_input("Ask a question:")

if query:
    context, results = retrieve_context(query)

    if not results:
        st.write("No relevant documents found.")
    else:
        answer = generate_answer(context, query)
        st.subheader("Answer:")
        st.write(answer)
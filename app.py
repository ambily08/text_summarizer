import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("Text Summarizer")
st.write("Summarize long paragraphs or articles using a Transformer-based model.")

with st.expander("Example Text"):
    st.code("""Artificial Intelligence (AI) is transforming the world rapidly. From self-driving cars to AI chatbots, the technology is reshaping how humans interact with machines. 
It is being applied across various industries including healthcare, finance, transportation, and education. With the continuous advancement in AI research and development, 
the possibilities are virtually endless. However, ethical concerns and regulatory challenges remain key issues that need to be addressed.""")

user_input = st.text_area("Enter text to summarize", height=200, placeholder="Paste or type your text here...")

max_len = st.slider("Maximum summary length", 50, 300, 130)
min_len = st.slider("Minimum summary length", 10, 100, 30)

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        summary = summarize_text(user_input, max_length=max_len, min_length=min_len)
        st.success("Summary:")
        st.write(summary)

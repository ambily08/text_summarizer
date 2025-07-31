from transformers import pipeline

# Load Hugging Face summarization pipeline
summarizer_pipeline = pipeline("summarization")

def summarize_text(text, max_length=130, min_length=30):
    if not text.strip():
        return "Please enter some text to summarize."
    summary = summarizer_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

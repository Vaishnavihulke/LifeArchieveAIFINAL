from transformers import pipeline
from sentence_transformers import SentenceTransformer

# Image caption model
captioner = pipeline("image-to-text")

# Text embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def generate_caption(image_path):
    result = captioner(image_path)
    return result[0]['generated_text']

def get_embedding(text):
    return embedder.encode(text)

def generate_tags(text):
    words = text.split()
    return ["#" + w for w in words[:3]]
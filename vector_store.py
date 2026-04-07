import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

memory_texts = []

def add_memory(embedding, text):
    global memory_texts
    index.add(np.array([embedding]).astype('float32'))
    memory_texts.append(text)

def search_memory(query_embedding):
    D, I = index.search(np.array([query_embedding]).astype('float32'), k=5)
    
    results = []
    for i in I[0]:
        if i < len(memory_texts):
            results.append(memory_texts[i])
    
    return results
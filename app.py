from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from model import generate_caption, get_embedding
from vector_store import add_memory, search_memory

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    caption = generate_caption(filepath)
    embedding = get_embedding(caption)

    add_memory(embedding, caption)

    return jsonify({"caption": caption})

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")

    embedding = get_embedding(query)
    results = search_memory(embedding)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

    @app.route("/chat", methods=["POST"])
 def char():
    data = request.json
    query = data.get("query")

    embedding = get_embedding(query)
    results = search_memory(embedding)

    answer = "Here’s what I found:\n"
    for r in results:
        answer += "- " + r + "\n"

    return jsonify({"response": answer})
 tags = generate_tags(caption)
    return jsonify({
    "caption": caption,
    "tags": tags
 })
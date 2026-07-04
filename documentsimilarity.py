from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Read the document
with open("document.txt", "r", encoding="utf-8") as file:
    document = file.read()

# Split document into paragraphs
chunks = [chunk.strip() for chunk in document.split("\n") if chunk.strip()]

# Generate embeddings for all chunks
document_embeddings = embedding.embed_documents(chunks)

# Ask the user a question
question = input("Enter your question: ")

# Generate embedding for the question
question_embedding = embedding.embed_query(question)

# Calculate cosine similarity
scores = cosine_similarity(
    [question_embedding],
    document_embeddings
)[0]

# Find the most similar chunk
best_index = scores.argmax()

print("\n" + "=" * 50)
print("Most Relevant Text:\n")
print(chunks[best_index])

print("\nSimilarity Score:")
print(round(scores[best_index], 3))
print("=" * 50)
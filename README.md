# 📄 Document Similarity Search using LangChain

A simple GenAI project that performs **semantic document similarity search** using **LangChain**, **Sentence Transformers**, and **Cosine Similarity**.

Instead of searching for exact keywords, the project understands the meaning of the user's question and returns the most relevant text from the document.

---

## 🚀 Features

- 📄 Reads a text document (`document.txt`)
- ✂️ Splits the document into chunks
- 🧠 Generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- 🔍 Performs semantic search using Cosine Similarity
- ✅ Returns the most relevant text along with its similarity score
- 💯 Runs completely locally (No OpenAI API required)

---

## 🛠️ Tech Stack

- Python
- LangChain
- Hugging Face Embeddings
- Sentence Transformers
- Scikit-Learn
- NumPy

---

## 📂 Project Structure

```
document-similarity-search/
│
├── app.py
├── document.txt
├── requirements.txt
├── README.md
└── screenshots/
    └── output.png
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/document-similarity-search.git
```

Go to the project folder

```bash
cd document-similarity-search
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

Example

```
Enter your question:
What is Machine Learning?

Most Relevant Text:

Machine Learning is a subset of Artificial Intelligence.

Similarity Score:
0.773
```

---

## 📚 Concepts Learned

- LangChain Embeddings
- Sentence Transformers
- Semantic Search
- Cosine Similarity
- Document Embeddings
- Natural Language Processing (NLP)

---

## 🔮 Future Improvements

- Support PDF and DOCX files
- Add FAISS Vector Database
- Retrieve Top-K Similar Chunks
- Build a RAG Pipeline
- Add a Streamlit Web Interface

---

## 👨‍💻 Author

**Omkar Narsale**

If you found this project helpful, feel free to ⭐ the repository.

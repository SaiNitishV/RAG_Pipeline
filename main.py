from load_data import load_pdf, chunk_text
from vector_store import VectorStore
from generator import generate_answer

# 1. Load and chunk documents
pdf_text = load_pdf("L6.pdf")
chunks = chunk_text(pdf_text)

# 2. Index in vector store
store = VectorStore()
store.add_texts(chunks)

# 3. Ask a question
while True:
    query = input("\Ask a question: or type exit ")
    if query.lower() == "exit":
        break

    context = store.search(query, k=4)
    answer = generate_answer(query, context)
    print("\n🤖 Answer:\n", answer)
import faiss
import numpy as np
from embedder import embed_text

class VectorStore:
    def __init__(self, dim=1536):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add_texts(self, texts):
        embeddings = [embed_text(t) for t in texts]
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

    def search(self, query, k=3):
        query_vec = np.array([embed_text(query)]).astype("float32")
        _, I = self.index.search(query_vec, k)
        return [self.texts[i] for i in I[0]]

if __name__ == "__main__":
    store = VectorStore()
    test_chunks = [
        "Our vacation policy allows 15 days per year.",
        "Employees must submit leave requests two weeks in advance.",
        "Healthcare benefits begin after 90 days."
    ]
    store.add_texts(test_chunks)

    results = store.search("How many vacation days do I get?")
    for r in results:
        print("Match:", r)
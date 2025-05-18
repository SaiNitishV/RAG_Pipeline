import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_text(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# ✅ Test
if __name__ == "__main__":
    sample = "Employees are entitled to 15 days of paid vacation annually."
    vec = embed_text(sample)
    print(f"Vector length: {len(vec)}")
    print("Sample values:", vec[:5])
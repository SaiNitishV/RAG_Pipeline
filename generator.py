import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    messages = [
        {"role": "system", "content": "You are an assistant."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # use gpt-4 if you have access
        messages=messages
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    fake_context = [
        "Employees are allowed 15 vacation days per year.",
        "Leave must be applied for in advance."
    ]
    query = "How much time off do I get per year?"
    print("Answer:\n", generate_answer(query, fake_context))
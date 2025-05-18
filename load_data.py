from PyPDF2 import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def chunk_text(text, max_tokens=300):
    sentences = text.split('. ')
    chunks, chunk = [], ""
    for sentence in sentences:
        if len(chunk.split()) + len(sentence.split()) < max_tokens:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "
    if chunk:
        chunks.append(chunk.strip())
    return chunks

if __name__ == "__main__":
    pdf_text = load_pdf("L6.pdf")
    chunks = chunk_text(pdf_text)
    print(f"Total chunks: {len(chunks)}")
    print("Sample chunk:\n", chunks[0])
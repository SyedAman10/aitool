import os
import json
import pdfplumber
from docx import Document

# Paths


# Dynamically resolve the documents directory relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCUMENTS_DIR = os.path.join(BASE_DIR, "../data/documents")
OUTPUT_FILE = os.path.join(BASE_DIR, "../data/processed_data.json")


def extract_pdf_text(file_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_word_text(file_path):
    """Extract text from a Word file."""
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def process_documents(doc_dir):
    """Process all documents in the directory and return structured data."""
    structured_data = []
    for filename in os.listdir(doc_dir):
        file_path = os.path.join(doc_dir, filename)
        if filename.endswith(".pdf"):
            content = extract_pdf_text(file_path)
        elif filename.endswith(".docx"):
            content = extract_word_text(file_path)
        else:
            continue
        
        structured_data.append({
            "file_name": filename,
            "content": content.strip()
        })
    return structured_data

def save_to_json(data, output_path):
    """Save structured data to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    data = process_documents(DOCUMENTS_DIR)
    save_to_json(data, OUTPUT_FILE)
    print(f"Data saved to {OUTPUT_FILE}")


from dotenv import load_dotenv
import os
import json
import openai
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Resolve paths dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "../data/processed_data.json")

def load_data(file_path):
    """Load structured data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_relevant_context(question, data):
    """Find the most relevant context and truncate to fit token limits."""
    for item in data:
        if question.lower() in item["content"].lower():
            return item["content"][:2000]  # Limit to 2000 characters
    return None  # Return None if no relevant context is found

def answer_question_openai(question, context=None):
    """Use OpenAI API to answer a question with or without context."""
    if context:
        messages = [
            {"role": "system", "content": "You are a helpful assistant for students."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"}
        ]
    else:
        # Fallback: General AI response without context
        messages = [
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": f"Question: {question}\nAnswer:"}
        ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=300,  # Limit output tokens
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    # Load and preprocess data
    data = load_data(DATA_FILE)

    print("AI Assistant Ready! Type 'exit' to quit.")
    while True:
        user_question = input("\nAsk a question: ").strip()
        if user_question.lower() == "exit":
            print("Goodbye!")
            break

        # Step 1: Search for relevant context
        context = find_relevant_context(user_question, data)

        try:
            # Step 2: Provide an answer (with or without context)
            if context:
                print("Context found! Answering based on the data...")
            else:
                print("No relevant context found. Answering with general knowledge...")

            answer = answer_question_openai(user_question, context)
            print(f"Answer: {answer}")
        except openai.error.OpenAIError as e:
            print(f"Error: {e}")

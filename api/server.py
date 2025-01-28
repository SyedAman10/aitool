from flask import Flask, request, jsonify
from dotenv import load_dotenv

import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data.get('question')
    
    # Use the chat completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=150
    )
    
    # Extract the answer from the response
    answer = response['choices'][0]['message']['content'].strip()
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

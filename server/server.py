from flask import Flask, request, jsonify
import openai
import os

openai.api_key ="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"

app = Flask(__name__)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data.get('question')
    
    # Use the chat completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",
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

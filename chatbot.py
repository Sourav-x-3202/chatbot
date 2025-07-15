#.\.venv\Scripts\activate
#1tem  ollama run gemma:2b
#2tem python chatbot.py 
#html run

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable frontend access from browser

chat_history = []  # To store context

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')

    # Add user message to history
    chat_history.append(f"User: {user_input}")

    # Format the full context
    full_prompt = "\n".join(chat_history) + "\nBot:"

    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'gemma:2b',
                'prompt': full_prompt,
                'stream': False
            }
        ).json()

        bot_reply = response.get('response', '').strip()

        # Add bot response to history
        chat_history.append(f"Bot: {bot_reply}")

        return jsonify({'response': bot_reply})

    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000)

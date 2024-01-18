from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

api_key = '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'  
api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-chat', methods=['POST'])
def generate_chat():
    user_input = request.json['message']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'prompt': user_input,
        'max_tokens': 150,
    }

    try:
        response = requests.post(api_url, json=data, headers=headers)
        generated_text = response.json()['choices'][0]['text']
        return jsonify({'generatedText': generated_text})
    except Exception as e:
        print('Error making API request:', e)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run()
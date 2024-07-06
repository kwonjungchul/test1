# app.py

from flask import Flask, request, jsonify, render_template
import openai
import logging

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = 'sk-proj-inMfFU0kNpnXbKsjYSnuT3BlbkFJLokgn8dfZflTBAgUoclf'

# 로그 파일 설정
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    try:
        data = request.json
        code = data.get('code')

        logging.info(f"Received code: {code}")

        prompt = f"Analyze the following Python code for any errors and suggest fixes:\n\n{code}\n\nProvide the corrected code and explain the changes. Additionally, check if the code follows PEP8 guidelines and provide any necessary corrections. Explain the functionality of the code. Suggest any possible optimizations."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        result = response.choices[0].message['content'].strip()

        logging.info(f"Analysis result: {result}")

        return jsonify({"result": result})
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)

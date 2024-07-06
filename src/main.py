# main.py

import openai

# OpenAI API 키 설정
openai.api_key = 'sk-proj-inMfFU0kNpnXbKsjYSnuT3BlbkFJLokgn8dfZflTBAgUoclf'

def analyze_and_fix_code(code):
    prompt = f"Analyze the following Python code for any errors and suggest fixes:\n\n{code}\n\nProvide the corrected code and explain the changes."
    
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    return response.choices[0].text.strip()

# 테스트 코드
code_sample = """
def add_numbers(a, b):
return a + b
"""

fixed_code = analyze_and_fix_code(code_sample)
print("Fixed Code:\n", fixed_code)

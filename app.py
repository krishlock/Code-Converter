import os

from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "sk-proj-cpyPRO0DD2w6d89EZXT3T3BlbkFJDzaNNCW8ml8Rl4JZs6US"
openai.api_base = "https://api.openai.com/v1/chat/completions"

# Define the supported languages
supported_languages = ["Cobol", "Delphi", "Vb.net"]

supported_languages2 = ["Python", "Java", "C#"]

@app.route('/')
def index():
    return render_template('index.html', languages=supported_languages,languages2=supported_languages2)

@app.route('/convert', methods=['POST'])
def convert():
    input_language = request.form['input-language']
    output_language = request.form['output-language']
    input_code = request.form['input-code']

    # Construct prompt for Chat Completions API

    # Construct prompt for Chat Completions API
    #prompt = f"Translate this function from {input_language} into {output_language} ### {input_language} \n\n {input_code} \n\n ### {output_language}"

    #prompt = f"Translate this function from {input_language} into {output_language}.\n\nInput ({input_language}): \n\n{input_code}\n\nOutput ({output_language}):"

    prompt = f"Translate the following {input_language} code into {output_language}.\n\n{input_language} Code:\n\n{input_code}\n\n{output_language} Code:"


    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=1050,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
    )


    


    # Extract code from the response
    output_code = response.choices[0].text.strip()

   # output_code = response.choices[0].text.strip().replace('{output_code}', '').strip()




    return output_code
if __name__ == '__main__':
    app.run(debug=True)
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.environ.get('OPENAI_API_KEY')


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        userInput = request.form["userInput"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(userInput),
            temperature=1,
            max_tokens=64,
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(userInput):
    return """Provide context for userInput.
userInput:provide a context to drinking tea
context:Drinking tea is often associated with relaxation and comfort. Many people enjoy a cup of tea in the morning to start their day, or in the evening to wind down after a long day at work. Tea can be a great way to take a break from the hustle and bustle of daily life, and to savor a moment of peace and tranquility.
userInput: {}
context:""".format(
        userInput.capitalize()
    )

from flask import Flask, request, jsonify
from flask_cors import CORS
from quizhelper import create_questions

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/generate", methods=['POST'])
def generate():
    data = request.get_json(force=True)
    title = data['title']

    questions = create_questions(title)
    return jsonify(questions)


if __name__ == "__main__":
    app.run()

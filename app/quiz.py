from flask import Flask
from flask_cors import CORS
import wikipedia as wiki

app = Flask(__name__)
CORS(app)


print (wiki.summary("donkey", auto_suggest=False))
print (wiki.page("donkey", auto_suggest=False).content)

@app.route("/")
def hello():
    return "Hello World"





if __name__ == "__main__":
    app.run()

from flask import Flask
from flask_cors import CORS
import wikipedia as wiki

app = Flask(__name__)
CORS(app)


def get_info(name):
    return wiki.summary(name)
    

@app.route("/")
def hello():
    return "Hello World"


print(get_info('whale'))


if __name__ == "__main__":
    app.run()

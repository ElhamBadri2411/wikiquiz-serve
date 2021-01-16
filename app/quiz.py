from flask import Flask
import wikipedia as wiki

app = Flask(__name__)

def get_info(name):
    return wiki.summary(name)
    

@app.route("/")
def hello():
    return "Hello World"

print(get_info('whale'))
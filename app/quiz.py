from flask import Flask
from wikipedia import wiki
app = Flask(__name__)

def get_info(name):
    return wiki.summary(name)
    

@app.route("/")
def hello():
    return "Hello World"

get_info('whale')
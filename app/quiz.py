from flask import Flask
import wikipedia as wiki

app = Flask(__name__)

def get_info(name):
    return 
    

@app.route("/")
def hello():
    return "Hello World"

print(get_info('wha le'))
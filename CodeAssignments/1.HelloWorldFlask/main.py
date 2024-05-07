#THIS IS A HELLO WORLD WITH FLASK
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World Flask'

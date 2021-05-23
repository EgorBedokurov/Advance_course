import datetime
import random
import string

from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    return "<p>Hello!!!</p>"

@app.route("/now")
def now():
    return str(datetime.datetime.now())

@app.route("/now")
def getrandom():
    return ''.join(random.choices(string.ascil_lowercase, k=10))

app.run(debug=True)

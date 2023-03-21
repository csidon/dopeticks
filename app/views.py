# This is where routes are defined

from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World! This is where we talk about how great our app is and tell people to sign up/login"


@app.route("/register")
def register():
    return "Registration page goes here"
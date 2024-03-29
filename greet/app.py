from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    return "<h1>WELCOME</h1>"


@app.route('/welcome/home')
def welcome_home():
    return f"<h1>WELCOME HOME!!</h1>"


@app.route('/welcome/back')
def welcome_back():
    return "<h1>WELCOME BACK!!!</h1>"
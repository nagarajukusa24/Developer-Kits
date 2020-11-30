# from flask import flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "hell...!"

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('user/<username>')
def user(username):
    return "User %s" % username

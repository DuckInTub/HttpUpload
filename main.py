from flask import Flask, render_template, session

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, world!</p>"

@app.route("/test")
def test():
    return "Test!"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/file/<string:hash>")
def upload():
    return render_template("upload.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")
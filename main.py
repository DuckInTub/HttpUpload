from flask import Flask, redirect, render_template, request, session, url_for
import db

app = Flask(__name__)
app.secret_key = "For testing now"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return "Test!"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":

        return render_template("login.html")

    username = request.form['username']
    password = request.form['password']

    if not db.validate_login(username, password):
        return render_template('login.html', error="No such user or incorrect password"), 400

    session["username"] = username
    return redirect(url_for("upload"))


@app.route("/logout")
def logout():
    if session:
        session.pop('username')
    return redirect(url_for('index'))

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/file/<string:hash>")
def file():
    return render_template("upload.html")


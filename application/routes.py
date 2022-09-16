import imp
from application import app 
from flask import render_template


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/Home")
def Home():
    return render_template("layout1.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

# index=True, login=True (goes in routes) ignore
from flask import Blueprint, render_template, url_for
index = Blueprint("index",__name__)

@index.route("/home")
def landing_page():
    print("Hello")
    return render_template("index.html")

@index.route("/hoom")
def poop():
    return render_template("index.html")
from flask import Blueprint, render_template, url_for
index = Blueprint("index",__name__)

@index.route("/hello")
def hello_world():
    return render_template("index.html")
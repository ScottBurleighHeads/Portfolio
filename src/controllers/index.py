from flask import Blueprint, render_template, url_for
index = Blueprint("index",__name__)

@index.route("/home")
def landing_page():
    return render_template("index.html")
from flask import Blueprint, render_template, url_for
aboutMe = Blueprint("aboutMe",__name__)

@aboutMe.route("/about")
def landing_page():
    return render_template("aboutMe.html")
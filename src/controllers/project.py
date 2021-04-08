from flask import Blueprint, render_template, url_for
project = Blueprint("project",__name__)

@project.route('/project')
def projectIndex():
    return render_template("projects.html")
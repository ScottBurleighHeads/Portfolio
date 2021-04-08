from flask import Blueprint, render_template, url_for
contact = Blueprint("contact",__name__)

@contact.route('/contact',methods=['GET'])
def contact_page():
    return render_template('contact.html')
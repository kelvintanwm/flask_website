from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/')
# @login_required
def home():
    """
    Home page of the website
    """
    return render_template("home.html")
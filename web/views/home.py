from flask import Blueprint, render_template


home_views = Blueprint('home', __name__, template_folder='../templates')

@home_views.route('/')
@home_views.route('/home')
@home_views.route('/index')
def home_view():
    return render_template('home.html')

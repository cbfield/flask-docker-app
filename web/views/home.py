from flask import Blueprint, render_template


views = Blueprint('home', __name__, template_folder='../templates')

@views.route('/')
@views.route('/home')
@views.route('/index')
def home_view():
    return render_template('home.html')

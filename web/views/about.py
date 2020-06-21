from flask import Blueprint, render_template


views = Blueprint('about', __name__, template_folder='../templates')

@views.route('/about')
def about_view():
    return render_template('about.html')
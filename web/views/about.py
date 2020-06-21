from flask import Blueprint, render_template


about_views = Blueprint('about', __name__, template_folder='../templates')

@about_views.route('/about')
def about_view():
    return render_template('about.html')
from flask import Blueprint, render_template
from web.middleware import get_redis_client

views = Blueprint('home', __name__, template_folder='../templates')

@views.route('/')
@views.route('/home')
@views.route('/index')
def home_view():
    client = get_redis_client()
    client.set('user','Kreestofer')
    user = client.get('user')

    return render_template('home.html',context = {'user': user})

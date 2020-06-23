from flask import Blueprint, render_template
from web.middleware import get_redis_client

from socket import gethostname
from random import getrandbits

views = Blueprint('home', __name__, template_folder='../templates')

@views.route('/')
@views.route('/home')
@views.route('/index')
def home_view():
    client = get_redis_client()
    client.set('a_value',getrandbits(10))
    a_value = client.get('a_value')
    print(a_value)

    return render_template('home.html',context = {'a_value': a_value,'host':gethostname()})

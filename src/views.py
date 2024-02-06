#!python3

import datetime
try:
    from flask import Blueprint, render_template
except ImportError as e:
    raise Exception(str(e))


home_view = Blueprint(
    'home', __name__, template_folder='templates', static_folder='static')


@home_view.route('/')
def home():
    return render_template('index.html')

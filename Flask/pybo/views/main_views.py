from flask import Blueprint, render_template

bp = Blueprint("main", __name__, url_prefix='/')

@bp.route('/')
def question():
    return 'hi hello'

@bp.route('/df')
def answer():
    return 'He iekrkk'
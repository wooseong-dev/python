from flask import Blueprint, render_template

bp = Blueprint("main", __name__, url_prefix='/')

@bp.route('/')
def question():
    return '은하야 안뇽 사랑해 '

@bp.route('/df')
def answer():
    return 'He iekrkk'

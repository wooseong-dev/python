from flask import Blueprint

city = Blueprint('city', __name__, url_prefix='/') # 블루 프린트 객체 생성

@city.route('/')
def question():
    return 'which one like u'

@city.route('/<name>')
def answer(name):
    return 'index' + name
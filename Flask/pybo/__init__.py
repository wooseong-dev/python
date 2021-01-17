from flask import Flask

from views import main_views


app=Flask(__name__)
app.register_blueprint('main',__name__ ,url_prefix='/')


def create_app():
    app=Flask(__name__)
    
    from .views import main_views
    app.register_blueprint(main_views.bp)

@app.route('/')    
def hello():
    return 'fuck u'

@app.route('/city')    
def question():
    return 'which one like u'

@app.route('/city/<name>')    
def answer(name):
    return 'fuck u' + name
    

if __name__ == "__main__":
    app.run(host='172.17.0.3', port=8000, debug=True)
    
    
    '''    
    from .views import main_views
    app.register_blueprint(main_views.bp)'''
from flask import Flask
from views import main_views
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config


db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.register_blueprint(main_views.bp)
app.config.from_object(config) # config에 작성한 항목을 app.config 환경변수로 부르기 위해 코드 추가

#ORM
db.init_app(app)#전역변수로 객체 생성
migrate.init_app(app,db)#전역변수로 객체 생성
#from . import models # question & answer 모델을 추가한 후 DB 가 변경되도록 flask db migrate 명령 수행

if __name__ == "__main__":
    app.run(host = '172.17.0.3', port=8000, debug=True)

    

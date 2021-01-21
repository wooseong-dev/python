from flask import Flask
from views import main_views

app = Flask(__name__)
app.register_blueprint(main_views.bp)

if __name__ == "__main__":
    app.run(host='172.17.0.22', port=8000, debug=True)

    

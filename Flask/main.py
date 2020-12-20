from flask import Flask
import sys
application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!"

if __name__ == "__main__":
    application.run(host='172.17.0.3', port=8000, debug=True)
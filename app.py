from flask import Flask
from flask import request, jsonify
from src.handlers.command_handler import CommandHandler

_ch = CommandHandler()
app = Flask(__name__)


@app.route('/add_user', methods = ['POST'])
def create_user():
    print(request.json)
    return _ch.insert_new_user(request.json)

@app.route('/get_user_by_email', methods = ['POST'])
def get_user_by_email():
    print(request.json)
    return _ch.find_user_by_email(request.json)


@app.route('/login', methods = ['POST'])
def login():
    print(request.json)
    return _ch.login(request.json)

@app.route('/test_mongo', methods = ['POST'])
def test_mongo():
    print(request.json)
    return _ch.test_mongo()

    
@app.errorhandler(404)
def not_found(error = None):
    response = jsonify(
        {
         'message' : 'Resource Not Found: ' + request.url
        }
    )
    response.status_code = 404
    return response

if __name__ == "__main__" :
    app.run(debug = True)
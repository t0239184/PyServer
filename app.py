from http.client import HTTPException
from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route("/ping", methods=["GET", "POST"])
def ping():
    return {"health": True}


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return {"error": "Http method not support."}, 400

    if not request.is_json:
        return {"error": "Request must be json format."}, 415

    request_data = request.get_json()
    if request_data:
        if ('account' not in request_data 
                or request_data['account'] == ''
                or 'password' not in request_data
                or request_data['password'] == ''):
            return {"error": "Account and Password is required."}, 500

        account = request_data['account']
        password = request_data['password']

    return {
        "account": account,
        "name": name
    }, 200
    

    


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


if __name__ == "__main__":
    app.run()

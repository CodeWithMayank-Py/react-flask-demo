from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    # Here you would validate the login credentials against your database
    if email == "test@example.com" and password == "password":
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

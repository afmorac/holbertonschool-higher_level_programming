from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario en memoria
users = {}

# Ruta raíz
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Ruta /status
@app.route('/status')
def status():
    return "OK"

# Ruta /data que devuelve solo los usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Ruta /users/<username>
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Ruta /add_user para POST
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()

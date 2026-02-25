from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import bcrypt
import jwt
import datetime
import os
import socket

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
PORT = int(os.getenv("PORT", 4000))

client = MongoClient(MONGO_URI)
db = client["taskmanager"]
users_collection = db["users"]

SECRET = "supersecretkey"


@app.route("/")
def home():
    hostname = socket.gethostname()
    return jsonify({"message": "Auth Service Running", "container": hostname})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if users_collection.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    users_collection.insert_one({
        "username": username,
        "password": hashed_pw,
        "skills": []
    })

    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({"username": username})

    if not user or not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET, algorithm="HS256")

    return jsonify({"token": token}), 200


@app.route("/profile", methods=["GET"])
def profile():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Token missing"}), 401

    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        username = decoded["username"]

        user = users_collection.find_one(
            {"username": username},
            {"_id": 0, "password": 0}
        )

        return jsonify(user)

    except:
        return jsonify({"error": "Invalid token"}), 401


@app.route("/add-skill", methods=["POST"])
def add_skill():
    token = request.headers.get("Authorization")
    data = request.get_json()
    skill = data.get("skill")

    if not token or not skill:
        return jsonify({"error": "Missing data"}), 400

    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        username = decoded["username"]

        users_collection.update_one(
            {"username": username},
            {"$push": {"skills": skill}}
        )

        return jsonify({"message": "Skill added"})

    except:
        return jsonify({"error": "Invalid token"}), 401


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
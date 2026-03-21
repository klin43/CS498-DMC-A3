from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.write_concern import WriteConcern
from pymongo.read_preferences import ReadPreference

app = Flask(__name__)

client = MongoClient("mongodb+srv://klin43_db_user:OuTCqg7OLR5jTFNR@cluster0.li7iy7j.mongodb.net/?appName=Cluster0")
db = client["ev_db"]
collection = db["vehicles"]

@app.route("/insert-fast", methods=["POST"])
def insert_fast():
    data = request.json
    fast_collection = collection.with_options(
        write_concern=WriteConcern(w=1),
        read_preference=ReadPreference.PRIMARY)
    result = fast_collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

@app.route("/insert-safe", methods=["POST"])
def insert_safe():
    data = request.json
    safe_collection = collection.with_options(
        write_concern=WriteConcern(w="majority"),
        read_preference=ReadPreference.PRIMARY)
    result = safe_collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

@app.route("/count-tesla-primary", methods=["GET"])
def count_tesla():
    primary_collection = collection.with_options(
        write_concern=WriteConcern(w="majority"),
        read_preference=ReadPreference.PRIMARY)
    count = primary_collection.count_documents({"Make": "Tesla"})
    return jsonify({"count": count})

@app.route("/count-bmw-secondary", methods=["GET"])
def count_bmw():
    secondary_collection = collection.with_options(
        write_concern=WriteConcern(w=1),
        read_preference=ReadPreference.SECONDARY)
    count = secondary_collection.count_documents({"Make": "BMW"})
    return jsonify({"count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

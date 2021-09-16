from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/projet")
db = mongo_client.db


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         user='myUserAdmin',
                         password='abc123',
                         authSource='admin')
    db = client["projet"]
    return db

@app.route('/')
def ping_server():
    todos = db.projet.find()
    return flask.jsonify([todo for todo in todos])

#@app.route('/users')
#def fetch_users():
#    db = get_db()
#    _users = db.projet.find()
#    users = [{"Name": user["Name"], "Position": user["Position"], "Age": user["Age"], "Team_from": user["Team_from"], "League_from": user["League_from"], "Team_to": user["Team_to"], "League_to": user["League_to"], "Season","Market_value": user["Season","Market_value"], "Transfer_fee": user["Transfer_fee"]} for user in _users]
#    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

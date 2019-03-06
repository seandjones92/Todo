#!/usr/bin/env python3

from flask import Flask, request, jsonify
import todopsql

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!" # This page should serv as API documentation

@app.route("/getall", methods=['GET'])
def getall():
    tododb = todopsql.connection()
    response = jsonify(tododb.getall())
    return response

@app.route("/createtask", methods=["POST"])
def createtask():
    if (request.method == 'POST') and (request.is_json):
        content = request.get_json()
        newtitle = content['title']
        newbody = content['body']
        tododb = todopsql.connection()
        tododb.createtask(newtitle, newbody)
        response = "Task created successfully"
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

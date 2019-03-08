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
        title = content['title']
        body = content['body']
        duedate = content['duedate']
        tododb = todopsql.connection()
        tododb.createtask(title, body, duedate)
        response = "Task created successfully"
        return response

@app.route("/completetask", methods=["PUT"])
def completetask():
    if (request.method == 'PUT') and (request.is_json):
        content = request.get_json()
        taskid = content['id']
        tododb = todopsql.connection()
        tododb.completetask(taskid)
        response = "Task completed"
        return response

@app.route("/deletetask", methods=["DELETE"])
def deletetask():
    if (request.method == 'DELETE') and (request.is_json):
        content = request.get_json()
        taskid = content['id']
        tododb = todopsql.connection()
        tododb.deletetask(taskid)
        response = "Task deleted"
        return response

@app.route("/echo", methods=["POST"])
def echorequest():
    if (request.method == 'POST') and (request.is_json):
        content = request.get_json()
        response = jsonify(content)
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

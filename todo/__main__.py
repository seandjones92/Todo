#!/usr/bin/env python3

from flask import Flask, request
import todopsql

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" # This page should serv as API documentation

@app.route("/getall", methods=['GET'])
def getall():
    tododb = todopsql.connection()
    results = str(tododb.getall())
    return results

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

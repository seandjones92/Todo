#!/usr/bin/env python3

import os
import json
import datetime
import psycopg2

class connection(object):
    def __init__(self):
        self.dbname = str(os.getenv('PSQL_DBNAME'))
        self.user = str(os.getenv('PSQL_USER'))
        self.password = str(os.getenv('PSQL_PASSWORD'))
        self.host = str(os.getenv('PSQL_HOST'))
        self.port = str(os.getenv('PSQL_PORT'))
        self.connstring = "dbname=%s user=%s password=%s host=%s port=%s" % (self.dbname, self.user, self.password, self.host, self.port)

    def getall(self):
        # Create connection and get cursor
        conn = psycopg2.connect(self.connstring)
        cur = conn.cursor()
        # Interact with DB
        cur.execute("SELECT * FROM todo;")
        mostrecent = cur.fetchall()
        # Close cursor and connection
        cur.close()
        conn.close()
        return mostrecent
    
    def createtask(self):
        # Create connection and get cursor
        conn = psycopg2.connect(self.connstring)
        cur = conn.cursor()
        # Interact with DB
        
        # Close cursor and connection
        cur.close()
        conn.close()

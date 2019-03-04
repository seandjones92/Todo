#!/usr/bin/env python3

import os
import psycopg2

class connection(object):
    def __init__(self):
        self.dbname = str(os.getenv('PSQL_DBNAME'))
        self.user = str(os.getenv('PSQL_DBNAME'))
        self.password = str(os.getenv('PSQL_PASSWORD'))
        self.host = str(os.getenv('PSQL_HOST'))
        self.port = str(os.getenv('PSQL_PORT'))
        self.connstring = "dbname=%s user=%s password=%s host=%s port=%s" % (self.dbname, self.user, self.password, self.host, self.port)

    def getmostrecent(self):
        conn = psycopg2.connect(self.connstring)
        cur = conn.cursor()
        cur.execute("SELECT * FROM todo;")
        mostrecent = cur.fetchall()
        cur.close()
        conn.close()
        return mostrecent

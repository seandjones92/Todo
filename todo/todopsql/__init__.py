#!/usr/bin/env python3

import os
import datetime
import psycopg2


class connection(object):
    def __init__(self):
        self.dbname = str(os.getenv('PSQL_DBNAME'))
        self.user = str(os.getenv('PSQL_USER'))
        self.password = str(os.getenv('PSQL_PASSWORD'))
        self.host = str(os.getenv('PSQL_HOST'))
        self.port = str(os.getenv('PSQL_PORT'))
        self.connstring = "dbname=%s user=%s password=%s host=%s port=%s" % \
            (self.dbname, self.user, self.password, self.host, self.port)

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

    def createtask(self, title, body, duedate):
        # Create connection and get cursor
        conn = psycopg2.connect(self.connstring)
        cur = conn.cursor()
        # Interact with DB
        if None not in (duedate['year'], duedate['month'], duedate['day']):
            cur.execute("INSERT INTO todo (title, body, createdon, duedate) " +
                        "VALUES ('%s', '%s', current_date, '%s');"
                        % (title, body, datetime.date(duedate['year'],
                                                      duedate['month'],
                                                      duedate['day'])))
        else:
            cur.execute("INSERT INTO todo (title, body, createdon) VALUES " +
                        "('%s', '%s', current_date);"
                        % (title, body))
        # Close cursor and connection
        cur.close()
        conn.commit()
        conn.close()

    def completetask(self, taskid):
        # add "current_date" to the "COMPLETEDON" row for the given task
        # UPDATE todo SET completedon = current_date WHERE id = 1;
        # Create connection and get cursor
        conn = psycopg2.connect(self.connstring)
        cur = conn.cursor()
        # Interact with DB
        cur.execute("UPDATE todo SET completedon = current_date WHERE id = %s;"
                    % (taskid))
        # Close cursor and connection
        cur.close()
        conn.commit()
        conn.close()

    def deletetask(self, taskid):
        # Create connection and get cursor
        conn = psycopg2.connect(self.connstring)
        cur = conn.cursor()
        # Interact with DB
        cur.execute("DELETE FROM todo WHERE id = %s;" % (taskid))
        # Close cursor and connection
        cur.close()
        conn.commit()
        conn.close()

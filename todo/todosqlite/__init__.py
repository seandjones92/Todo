#!/usr/bin/env python3

import datetime
import os
import sqlite3


class connection(object):
    """
    Handle SQLITE3 database interactions
    """

    def __init__(self):
        """
        initialize DB connection
        """
        self.conn = sqlite3.connect('/data/todo.db')

    def close(self):
        """
        close out connection to db
        """
        self.conn.close()

    def getall(self):
        """
        get all todo items
        """
        c = self.conn.cursor()
        c.execute("SELET * FROM todo;")
        c.close()


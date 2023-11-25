#!/usr/bin/env python3
"""A script that filters state by user input"""
import sys
import MySQLdb

if __name__ == "__main__":
    (_, username, password, dbname, state) = sys.argv
    port = 3306
    db = MySQLdb.connect(
        host='localhost', passwd=password,
        port=port, user=username, db=dbname
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' \
            ORDER BY states.id".format(state))
    rows = cur.fetchall()
    for entry in rows:
        print(entry)

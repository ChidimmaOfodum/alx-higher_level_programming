#!/usr/bin/env python3
"""A script that filters state by user input"""
import sys
import MySQLdb

if __name__ == "__main__":
    (_, username, password, dbname) = sys.argv
    port = 3306
    db = MySQLdb.connect(
        host='localhost', passwd=password,
        port=port, user=username, db=dbname
    )
    cur = db.cursor()
    cur.execute("SELECT cities.state_id, cities.name, states.name \
                FROM cities INNER JOIN states on cities.state_id = states.id \
                ORDER BY cities.id")
    rows = cur.fetchall()
    for entry in rows:
        print(entry)

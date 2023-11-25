#!/usr/bin/python3
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
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states on cities.state_id = states.id WHERE states.name = %s\
                ORDER BY cities.id", [state])
    rows = cur.fetchall()
    print(', '.join([str(y) for (_,y,_) in rows]))

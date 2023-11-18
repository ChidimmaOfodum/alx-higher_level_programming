#!/usr/bin/python3
# A script that connects to a mysql db and retrieves all states
import sys
import MySQLdb

if __name__ == "__main__":
    (_, username, password, dbname) = sys.argv
    db = MySQLdb.connect(
        host='localhost', passwd=password,
        port="3306", user=username, db=dbname
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for entry in rows:
        print(entry)

#!/usr/bin/python3
"""A script that retrieves all states starting with 'N'"""
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
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for entry in rows:
        if (entry[1][0] == "N"):
            print(entry)

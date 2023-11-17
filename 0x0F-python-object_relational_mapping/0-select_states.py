#!/usr/bin/python3
# A script that connects to a mysql db and retrieves all states
import sys
import MySQLdb

(_, username, password, dbname) = sys.argv
db = MySQLdb.connect(
    host='localhost', passwd=password, user=username, db=dbname
)

cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()

for entry in rows:
    print(entry)

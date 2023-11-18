#!/usr/bin/python3
import sys
import MySQLdb

(_, username, password, dbname, state) = sys.argv
port = 3306
db = MySQLdb.connect(
    host='localhost', passwd=password,
    port=port, user=username, db=dbname
)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name = %s", [state])
rows = cur.fetchall()
for entry in rows:
    print(entry)

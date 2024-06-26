#!/usr/bin/python3
"""A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
if __name__ == "__main__":
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""
                   SELECT id, name
                   FROM states
                   WHERE BINARY LEFT(name, 1)='N'
                   ORDER BY id ASC
                   """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

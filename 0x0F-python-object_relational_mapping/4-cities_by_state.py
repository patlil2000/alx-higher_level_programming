#!/usr/bin/python3

"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv
db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=argv[1],
                     passwd=argv[2],
                     db=argv[3])
cursor = db.cursor()
query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
db.close()

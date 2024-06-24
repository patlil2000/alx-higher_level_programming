#!/usr/bin/python3
""" a script that takes in arguments and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    query = """
            SELECT id, name
            FROM states
            WHERE name = %s
            ORDER BY id ASC
            """
    cursor.execute(query, (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

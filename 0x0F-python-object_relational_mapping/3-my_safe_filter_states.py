#!/usr/bin/env python3
"""
This module lists all states in a database
"""
import MySQLdb
import sys

if __name__ == "__main__":

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = """SELECT * FROM states WHERE name LIKE BINARY
     %s ORDER BY id ASC"""

    cursor.execute(query, (sys.argv[4],))

    for i in cursor.fetchall():
        print(i)

    cursor.close()
    connection.close()

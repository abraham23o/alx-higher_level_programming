#!/usr/bin/python3
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
     '{}' ORDER BY id ASC""".format(sys.argv[4])

    cursor.execute(query)

    for i in cursor.fetchall():
        print(i)

    cursor.close()
    connection.close()

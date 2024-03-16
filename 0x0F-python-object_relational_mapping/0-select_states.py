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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for i in cursor.fetchall():
        print(i)

    cursor.close()
    connection.close()

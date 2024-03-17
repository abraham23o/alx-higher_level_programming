#!/usr/bin/env python3
"""
This module lists all cities in a database
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

    query = """SELECT c.id, c.name, s.name
     FROM states s, cities c WHERE s.id = c.state_id ORDER BY c.id ASC"""

    cursor.execute(query)

    for i in cursor.fetchall():
        print(i)

    cursor.close()
    connection.close()

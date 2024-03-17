#!/usr/bin/python3
"""
This module lists all cities of state passed as
an argument in a database
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

    query = """SELECT c.name
     FROM states s INNER JOIN cities c ON s.id = c.state_id 
     WHERE s.name = %s ORDER BY c.id ASC"""

    cursor.execute(query, (sys.argv[4], ))

    attributes = cursor.fetchall()
    print(", ".join([city[0] for city in attributes]))

    cursor.close()
    connection.close()

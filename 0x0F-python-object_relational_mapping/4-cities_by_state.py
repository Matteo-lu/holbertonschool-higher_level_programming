#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa.

This Module is for the project 0x0F. Python - Object-relational
mapping proposed by Holberton school as a test for the implementation
of MySQLdb module with hbtn_0e_0_usa database.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    args_list = sys.argv
    username = args_list[1]
    password = args_list[2]
    database_name = args_list[3]

    db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=username,
                            passwd=password,
                            db=database_name
                            )

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities LEFT JOIN states \
                    ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()

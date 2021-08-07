#!/usr/bin/python3
""" script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
from the database hbtn_0e_0_usa.

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
    state_name = args_list[4]

    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=username,
                        passwd=password,
                        db=database_name
                        )

    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    try:
        cursor.execute("""SELECT * FROM states \
                        WHERE states.name = '{}' \
                        ORDER BY states.id ASC""".format(state_name))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("Error: unable to fecth data")

    db.close()

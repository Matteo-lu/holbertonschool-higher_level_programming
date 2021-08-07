#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.

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
                            port=3306, user=username,
                            passwd=password,
                            db=database_name
                            )

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name \
                    FROM cities LEFT JOIN states \
                    ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id""", (state_name,))

    results = cursor.fetchall()
    count = 0
    if len(results) > 0:
        for row in results:
            count += 1
            if count < (len(results)):
                print('{}, '.format(row[0]), end="")
            else:
                print('{}'.format(row[0]))
    else:
        print()

    db.close()

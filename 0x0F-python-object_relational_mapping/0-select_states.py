#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa

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

    cursor.execute("SELECT VERSION()")

    sql = "SELECT * FROM states \
            ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("Error: unable to fecth data")

    db.close()

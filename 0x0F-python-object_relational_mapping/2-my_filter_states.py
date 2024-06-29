#!/usr/bin/python3

"""
Modules Imported: sys, MySQLdb
sys: Library for executing shell commands from a pyscript
MySQLdb: Managing MySQL databases from a pyscript
"""
import sys
import MySQLdb


if __name__ == '__main__':
    searched = sys.argv[4]  # Entry to find and print fron db - Optional
    db_name = sys.argv[3]
    user_passwd = sys.argv[2]
    user_name = sys.argv[1]
    try:
        conn = MySQLdb.connect(
                host='localhost',
                user=user_name,
                passwd=user_passwd,
                db=db_name
        )
    except (Exception):
        print('Couldnt connect to the database')

    cur = conn.cursor()
    query = "SELECT * FROM states \
            WHERE name = '{}' \
            ORDER by id ASC".format(searched)
    cur.execute(query)

    table = cur.fetchall()
    for row in table:
        print(row)

    cur.close()
    conn.close()

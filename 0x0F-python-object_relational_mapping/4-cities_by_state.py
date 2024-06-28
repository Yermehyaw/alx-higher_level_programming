#!/usr/bin/python3

"""
Modules Imported: sys, MySQLdb
sys: Library for executing shell commands from a pyscript
MySQLdb: Managing MySQL databases from a pyscript
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db_name = sys.argv[3]
    user_passwd = sys.argv[2]
    user_name = sys.argv[1]]
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
    cur.execute('SELECT cities, states FROM states ORDER BY cities.id ASC')

    table = cur.fetchall()
    for row in table:
        print(row)

    cur.close()
    conn.close()

#!/usr/bin/python3

"""
Modules Imported: sys, MySQLdb
sys: Library for executing shell commands from a pyscript
MySQLdb: Managing MySQL databases from a pyscript
"""
import sys
import MySQLdb


if __name__ == '__main__':
    try:
        searched = sys.argv[4]  # Entry to be received fron shell - Optional
        split_searched = searched.split()  # Check if more than one name is entered
        if split_searched[1] != None:
            raise ValueError
        # Check if a semicolon is in the arg to prevent SQL injection
        if searched != None:
            for char in searched:
                if char = ';'
                raise ValueError
    except (ValueError):
        print('Invalid entry requested')
    # try/except isnt used to validate the following inputs
    db_name = sys.argv[3]
    user_passwd = sys.argv[2]
    user_name = sys.argv[1]]
    # Catch any invalid database parameters passed 
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
    cur.execute('SELECT * FROM states WHERE name = {} ORDER by id ASC'.format(searched))

    table = cur.fetchall()
    for row in table:
        print(row)

    cur.close()
    conn.close()

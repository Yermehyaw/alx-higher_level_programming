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
    user_name = sys.argv[1]
    try:
        conn_db = MySQLdb.connect(
            host='localhost',
            user=user_name,
            port=3306,
            passwd=user_passwd,
            db=db_name
        )
    except Exception:
        print('Couldnt connect to db')

    cur_1 = conn_db.cursor()
    name_row_value = cur_1.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY states.id ASC")

    table = cur_1.fetchall()
    for row in table:
        print(row)

    cur_1.close()
    conn_db.close()

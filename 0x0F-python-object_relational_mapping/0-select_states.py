#!/usr/bin/python3

"""
Modules Imported: sys, MySQLdb

sys
Library for executing shell commands from a pyscript

MySQLdb
Managing MySQL databases from apyscript

"""
import sys
import MySQLdb


if __name__ == '__main__':
    try:
        conn_db = MySQLdb.connect(host=localhost, user=sys.argv[1], port=3306
                                  passwd=sys.argv[2], db=sys.argv[3])
    except ():
        return (1)
    cur_1 = conn_db.cursor()
    name_row_value = cur_1.execute(f"SELECT * FROM {sys.argv[3]} ORDER BY\
states.id ASC")
    print(name_row_value)
    return (0)

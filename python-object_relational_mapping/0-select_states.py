#!usr/bin/python3
"""
This script lists all states from the
database 'hbtn_0e_0_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database
    """
    db = MySQLdb.connect(host='localhost', port=3306, username = argv[1], password = argv[2], db = argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
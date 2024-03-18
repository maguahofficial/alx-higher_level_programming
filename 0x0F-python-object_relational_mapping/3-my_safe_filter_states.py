#!/usr/bin/python3
""" The lists of all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curx = db.cursor()
    match = sys.argv[4]
    curx.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = curx.fetchall()
    for row in rows:
        print(row)
    curx.close()
    db.close()

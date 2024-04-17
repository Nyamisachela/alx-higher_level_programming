#!/usr/bin/python3
"""
A script that lists all states from the database `hbtn_0e_0_usa`
with names starting with 'N' using the MySQLdb module.
This script is designed to demonstrate database querying through Python using MySQLdb.

Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
Example: ./1-filter_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys

def main():
    """
    Main function that fetches and prints states from the database starting with 'N'.
    """
    mysql_username = sys.argv[1]  # The MySQL username
    mysql_password = sys.argv[2]  # The MySQL password
    database_name = sys.argv[3]   # The database name

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    
    for state in states:
        print(state)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()


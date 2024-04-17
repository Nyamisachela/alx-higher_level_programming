#!/usr/bin/python3
"""
A script that lists all states from the database `hbtn_0e_0_usa`.
This script demonstrates basic database access and data retrieval using the MySQLdb module.

Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
Example: ./0-select_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys

def main():
    """
    Main function that fetches states from the database and prints them sorted by id.
    """
    mysql_username = sys.argv[1]  # The MySQL username from the command line argument
    mysql_password = sys.argv[2]  # The MySQL password from the command line argument
    database_name = sys.argv[3]   # The database name from the command line argument

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",           # Host, typically localhost
        port=3306,                  # Port number, default to 3306
        user=mysql_username,        # Username as provided by the user
        passwd=mysql_password,      # Password as provided by the user
        db=database_name            # Database name
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()
    # Execute a SQL Query to select all states in ascending order by their IDs
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the results based on the executed query
    states = cur.fetchall()

    # Loop through each fetched entry and print it
    for state in states:
        print(state)

    # Close the cursor and the database connection to free resources
    cur.close()
    db.close()

if __name__ == "__main__":
    main()

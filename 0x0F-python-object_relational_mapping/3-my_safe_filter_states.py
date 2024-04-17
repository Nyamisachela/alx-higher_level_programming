#!/usr/bin/python3
import sys
import MySQLdb

def fetch_states(username, password, database, state_name):
    """
    Fetches states from the database that match the given state name safely to prevent SQL injection.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))  # Using parameterized inputs to prevent SQL injection

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        fetch_states(username, password, database, state_name)


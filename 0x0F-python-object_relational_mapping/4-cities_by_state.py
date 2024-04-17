#!/usr/bin/python3
import sys
import MySQLdb

def list_cities(username, password, database):
    """
    Lists all cities from the database sorted by city id.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(query)

    results


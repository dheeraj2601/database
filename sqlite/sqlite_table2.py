import os
import sys 
import sqlite3

db_filename = '/usr/local/etc/ABC_RD.db'
schema_filename = '/usr/local/etc/xyz.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

    cursor = conn.cursor()

    # Retrieving list of tables
    cursor.execute("""
    select name from sqlite_master where type = 'table';
    """)

    query = "delete from %s"

    for row in cursor.fetchall():
       if 'bgp' in row[0]:  
          cursor.execute(query % (row[0]))

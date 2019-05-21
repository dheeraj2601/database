import os
import sys
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'
table_name = sys.argv[1]

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
    for row in cursor.fetchall():
        print '%s' % (row[0])


    print '\n\n'
    # Retrieving schema of all tables
    cursor.execute("""
    select sql from sqlite_master where type = 'table'
    """)
    for row in cursor.fetchmany(5):
        print '%s' % ( row[0] )
        
    print '\n\n'
    
    # Retrieving schema    
    cursor.execute("select sql from sqlite_master where sql not NULL")
    for row in cursor.fetchall():
        print row[0]

    print '\n\n'
    # Retrieving schema of specific table
    query = "select sql from sqlite_master where type = 'table' and name = ?"
    cursor.execute(query, (table_name,))
    for row in cursor.fetchmany(5):
        print '%s' % ( row[0] )

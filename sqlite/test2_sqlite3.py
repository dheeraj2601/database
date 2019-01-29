import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserting initial data'

        conn.execute("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week', '2010-11-01')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2010-10-03', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2010-10-10', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2010-10-17', 'pymotw')
        """)
    else:
        print 'Database exists, assume schema does, too.'

    # Retrieving Data 

    cursor = conn.cursor()

    cursor.execute("""
    select id, priority, details, status, deadline from task where project = 'pymotw'
    """)
    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print '%2d {%d} %-20s [%-8s] (%s)' % (task_id, priority, details, status, deadline)

    print '\n\n'
    # fetchone 
    cursor.execute("""
    select name, description, deadline from project where name = 'pymotw'
    """)
    name, description, deadline = cursor.fetchone()

    print 'Project details for %s (%s) due %s' % (description, name, deadline)

    print '\n\n'
    # fetchmany
    cursor.execute("""
    select id, priority, status, deadline, details from task
    where project = 'pymotw' order by deadline
    """)

    print '\nNext 5 tasks:'

    for row in cursor.fetchmany(5):
        print '%2d {%d} %-25s [%-8s] (%s)' % (
            row[0], row[1], row[4], row[2], row[3],
            )

    print '\niterdump'
    for text in conn.iterdump():
        print text

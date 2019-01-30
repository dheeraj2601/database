# run as python sqlite_tables.py bgp_bgpPeer

import os
import sys
import sqlite3
import pandas as pd

db_filename = '/usr/local/etc/RD.db'
table_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:

       print pd.read_sql_query("SELECT * FROM %s" % table_name, conn)

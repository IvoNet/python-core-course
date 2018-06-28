#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# http://filldb.info/

# Authors note:
# run the mysqld in the mysql folder of this course
# change the ip host according to the host you are presenting from
#

import MySQLdb

db = MySQLdb.connect(host="192.168.2.242",
                     user="user",
                     passwd="secret",
                     db="test")

cursor = db.cursor()

print(cursor.execute("SELECT * FROM authors"))

# Commit your changes if writing
# In this case, we are only reading data
# db.commit()

# Get the number of rows in the resultset
# Get and display one row at a time
for x in range(0, cursor.rowcount):
    row = cursor.fetchone()
    print(row[0], "-->", row[1])

# Close the connection
db.close()


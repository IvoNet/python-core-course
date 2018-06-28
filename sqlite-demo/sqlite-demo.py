#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# http://www.sqlitetutorial.net/sqlite-sample-database/

import sqlite3

db = sqlite3.connect('chinook.db')
cursor = db.cursor()

for row in cursor.execute('SELECT * FROM tracks WHERE AlbumId = 1'):
    print(row)


# [print(x) for x in cursor.execute('SELECT DISTINCT AlbumId FROM albums where ArtistId = 1')]
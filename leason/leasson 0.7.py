# база данных
# 2 реляционные  и не реляционные
# SQL - язык структурированных запросов
# субд система управления базами данных
# oracle mySQL postgreSQL - SQLlite
# CRUD-create reed update delete

import sqlite3

db = sqlite3.connect('30_3.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS 
user(
name text,
title text,
view integer,
nick text
)''')

c.execute("INSERT INTO user VALUES "
          "('bekbolot','hello',40,'qwerty') ")

c.execute("UPDATE user SET name='aaaa' WHERE rowid <4 ")
c.execute("UPDATE user SET view=50 WHERE name='aaaa' ")
c.execute("update user set view=10 WHERE rowid>2")
c.execute("DELETE FROM user WHERE view <>40 ")

c.execute("SELECT rowid,* FROM user")
item = c.fetchall()
for i in item:
    print(i)

db.commit()
db.close()
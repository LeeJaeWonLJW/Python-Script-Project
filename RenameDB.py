import pymysql.cursors
import string
import random
import os

def id_generator(size, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def db_conn(db_host='localhost', db_user='', db_password='', db_db='', db_charset='utf8mb4'):
    return pymysql.connect(host=db_host,
                       user=db_user,
                       password=db_password,
                       db=db_db,
                       charset=db_charset)

def dbPrint(rows, want):
    for row in rows:
        return row[want]

def query_select(column='*',table=''):
    return "SELECT" + column + "FROM " + table + ""

def query_update(column='',table='',where='',set=''):
    return "UPDATE " + table + " SET " + column + "='" + set + "'" + " WHERE " + column + "=" + "'" + where + "'"

#MySQL Connection Info
conn = db_conn('Server','ID','PW','DB','Encoding Format')

#Make MySQL Cursor
curs = conn.cursor(pymysql.cursors.DictCursor)

#SQL Query
sql = query_select('*','Page')
curs.execute(sql)

"""
MySQL List
 - mainpage
"""

mainpage = dbPrint(curs.fetchall(),'mainpage')
NewName=id_generator(10)
curs.execute(query_update('mainpage', 'Page', mainpage, NewName))
conn.commit()
conn.close()

os.rename(mainpage+".html", NewName+".html")


import mariadb
from flask import g
import sys

def get_db():
    con = getattr(g, '_database', None)
    if con is None:
        con = mariadb.connect(
            host='192.168.1.11',
            port= 3306,
            user='root',
            password='rootroot',
            database='VelocityAppDB')
        print(con, file=sys.stderr)
    return con

def get_cur():
    cur = getattr(g, '_cursor', None)
    if cur is None:
        cur = get_db().cursor()
    return cur

def db_connection(instruction):
    try:
        #print(get_cur, file=sys.stderr)
        print(instruction, file=sys.stderr)
        sql_result = get_cur().execute(instruction)            
        get_db().commit()
        print(sql_result, file=sys.stderr)
        return sql_result
    except mariadb.Error as e: 
        print(f"Error: {e}")
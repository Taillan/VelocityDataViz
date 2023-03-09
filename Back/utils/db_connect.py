
import mariadb
from flask import g, jsonify 
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
    return con

def get_cur():
    cur = getattr(g, '_cursor', None)
    if cur is None:
        cur = get_db().cursor()
    return cur

def db_connection(instruction):
    try:
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute(instruction)
            db.commit()
            if(cursor.description != None):
                return  cursor.fetchall()
    except mariadb.Error as e: 
        print(f"Error db_connection : {e}")
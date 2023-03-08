from utils.db_connect import db_connection,get_cur
import sys

def saveUser(User):
    instruction = f'insert into Account (username,password,email) values ("{User.username}","{User.password}","{User.email}")'
    db_connection(instruction)
    return get_cur().lastrowid

def updateUser(User, id):
    instruction =   f'update Account set username="{User.username}", password="{User.password}", email="{User.email}" where id={id}'
    return db_connection(instruction)
    
def getUser(id):    
    instruction = f'select * from Account where id={id}'
    return db_connection(instruction).fetchone()

def getAllUser():
    instruction = f'select * from Account;'
    return db_connection(instruction)

def deleteUser(id):
    instruction = f'delete from Account where id={id}'
    return db_connection(instruction)

def deleteAllUser():
    instruction = f'delete from Account'
    return db_connection(instruction)
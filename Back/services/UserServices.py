from models.User import User
from utils.errors import NotFound
from utils.db_connect import get_cur
from dao.UserDAO import *

def NewUserService(payload):
    user = UserFromJson(payload)

    saveUser(user)
    return user

def GetUserService(position):
    sql_result = getUser(position)

    if sql_result == None:
        raise NotFound

    User = UserFromSQL(sql_result)
    return User

def GetAllUserService():
    return getAllUser()

def UpdateUserService(id, payload):
    user = UserFromJson(payload)
    return updateUser(user, id)

def DeleteUserService(id):
    deleteUser(id)

    if get_cur.rowcount == 0:
        raise NotFound

def DeleteAllUsers():
    deleteAllUser()

def UserFromJson(payload):
    #print(payload, file=sys.stderr)
    try:
        username = payload['username']
    except:
        return "Missing username field"
    try:
        password = payload['password']
    except:
        return "Missing password field"
    try:
        email = payload['email']
    except:
        return "Missing email field"
    return User(username, password,email)

def UserFromSQL(payload):
    try:
        id = payload[0]
    except:
        return "Missing id"
    try:
        username = payload[1]
    except:
        return "Missing username"
    try:
        password = payload[2]
    except:
        return "Missing password"
    try:
        email = payload[3]
    except:
        return "Missing email"
    return User(username, password,email,id)

def AllUserFromSQL(payload):
    users = []
    for user in payload:
        users.append(UserFromSQL(user))
    return users

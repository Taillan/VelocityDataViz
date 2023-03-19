from flask import Blueprint
from flask import request
from utils.errors import *
from services.UserServices import *
import json

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['POST'])
def NewUser():
	payload = request.get_json()
	try:
		user = NewUserService(payload)
		return user.toJSON(), 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@user_blueprint.route('/users', methods=['DELETE'])
def DelAllUser():
	try:
		DeleteAllUsers()
		return ALL_USER_DELETED_MESSAGE, 204
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
		
@user_blueprint.route('/users', methods=['GET'])
def GetAllUsers():
	try:
		users = json.dumps([ u.toJSON() for u in GetAllUserService()])
		return users, 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 

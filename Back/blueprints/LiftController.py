from flask import Blueprint
from flask import request
from utils.errors import *
from services.LiftServices import *

lift_blueprint = Blueprint('lift', __name__)

@lift_blueprint.route('/lift', methods=['POST'])
def NewUser():

	payload = request.get_json()
	try:
		lift = NewLiftService(payload)
		return lift.toJSON(), 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@lift_blueprint.route('/lifts', methods=['DELETE'])
def DelAllLift():
	try:
		DeleteAllLifts()
		return ALL_USER_DELETED_MESSAGE, 204
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 

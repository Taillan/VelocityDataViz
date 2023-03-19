from flask import Blueprint
from flask import request
from utils.errors import *
from services.LiftServices import *
import json

lift_blueprint = Blueprint('lift', __name__)

@lift_blueprint.route('/lift', methods=['POST'])
def NewLift():
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

@lift_blueprint.route('/lifts', methods=['GET'])
def GetAllLifts():
	try:
		for u in GetAllLiftService():
			print(u, file=sys.stderr)
		lifts = json.dumps([ lift.toJSON() for lift in GetAllLiftService()])
		return lifts, 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 

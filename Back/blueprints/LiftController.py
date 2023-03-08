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

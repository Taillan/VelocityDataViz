import json
from flask import Flask, request
from services.UserServices import *
from services.LiftServices import *
from utils.errors import *
from flask_cors import CORS
from blueprints.UserController import user_blueprint
from blueprints.LiftController import lift_blueprint
from utils.db_connect import get_db, get_cur
from utils.db_connect import db_connection

app = Flask(__name__)
app.debug=True
app.register_blueprint(user_blueprint)
app.register_blueprint(lift_blueprint)
CORS(app)

#print(Lift.Set, file=sys.stderr) Faut bien le noter qq part
@app.route('/users', methods=['GET'])
def GetAllUsers():
	return GetAllUserService(), 200

@app.route('/lifts', methods=['GET'])
def GetAllLifts():
	return GetAllLiftService(), 200

if __name__ == "__main__":
	with app.app_context():
		get_db()
		get_cur()
	app.run()

	
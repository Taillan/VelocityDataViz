import json
from flask import Flask, request
from services.UserServices import *
from utils.errors import *
from flask_cors import CORS
from blueprints.UserController import user_blueprint
from utils.db_connect import get_db, get_cur
from utils.db_connect import db_connection

app = Flask(__name__)
app.debug=True
app.register_blueprint(user_blueprint)
CORS(app)

@app.route('/users', methods=['GET'])
def GetAllUsers():
	return GetAllUserService(), 200

if __name__ == "__main__":
	with app.app_context():
		get_db()
		get_cur()
	app.run()
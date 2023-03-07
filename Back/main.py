from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json
import mariadb


app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

con = mariadb.connect(
         host='192.168.1.11',
         port= 3306,
         user='root',
         password='rootroot',
         database='VelocityAppDB')
cur = con.cursor()

@app.route("/index")
def index():
    return "Connected to database"

class Users(Resource):
    def get(self):
        try: 
            cur.execute("SELECT * FROM `Account`")
            row_headers=[x[0] for x in cur.description] #this will extract row headers
            rv = cur.fetchall()
            json_data=[]
            for result in rv:
                    json_data.append(dict(zip(row_headers,result)))
            return json_data, 200 
        except mariadb.Error as e: 
            print(f"Error: {e}")

    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            print('content_type', file=sys.stderr)
            json = request.json
            
            #cur.execute("INSERT INTO `Account` (`userId`, `Username`, `passowrd`, `Email`) VALUES (NULL, '"+json.username+"', '"+json.password+"', '"+json.email+"');")
        return {'OK'}, 200  # return data with 200 OK
    
class DataLift(Resource):
    def get(self):
        try: 
            cur.execute("SELECT * FROM `DataLift`")
            row_headers=[x[0] for x in cur.description] #this will extract row headers
            rv = cur.fetchall()
            json_data=[]
            for result in rv:
                    json_data.append(dict(zip(row_headers,result)))
            return json_data
        except mariadb.Error as e: 
            print(f"Error: {e}")
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(DataLift, '/datalift')  # and '/locations' is our entry point for Locations


if __name__ == '__main__':
    app.run()  # run our Flask app
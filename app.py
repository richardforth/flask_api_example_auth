from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

api = Api(app)

jwt = JWT(app,authenticate,identity)

class HelloWorld(Resource):

	@jwt_required()
	def get(self):
		return {'hello': 'world'}

api.add_resource(HelloWorld, '/')


if __name__ == "__main__":
	app.run(debug=True)

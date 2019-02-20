import sqlite3
from flask_restful import Resource, reqparse
from model.user import UserModel

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help="this field cannot be null"
		)

	parser.add_argument('password',
		type=str,
		required=True,
		help="this field cannot be null"
		)
	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):
			return {'message': 'that username already exist'}, 400

		user = UserModel(**data)#(data['username'], data['password'])
		user.add_to_db()
		return {'message': 'user registered successfully'}, 201

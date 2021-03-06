from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.item import ItemModel

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
			type=float,
			required=True,
			help= "this field cannot be empty"
			)

	parser.add_argument('store_id',
			type=int,
			required=True,
			help= "every item need a store id"
			)
	@jwt_required()
	def get(self,name):
		item = ItemModel.find_by_name(name)
		if name:
			return item.json()
		return {'message': 'item not found'}, 404

	
	def post(self,name):
		if ItemModel.find_by_name(name):
			return {'message': "an item with name '{}' already exist.".format(name)}, 400

		data = Item.parser.parse_args()

		item = ItemModel(name, **data)# **data simplifies data['price'], data['store_id']

		try:
			item.add_to_db()
		except:
			return {'message': 'Error occured while inserting item'}, 500
			

		return item.json(), 201

	def delete(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()

		return {'message': 'item deleted'}

	def put(self, name):
		
		data = Item.parser.parse_args()

		item = ItemModel.find_by_name(name)
		

		if item is None:
			ItemModel(name, **data)
		else:
			item.price = data['price']
			item.store_id = data['store_id']
			
		item.add_to_db()
		return item.json()

	
class Itemlist(Resource):
	def get(self):
		return {'items': [x.json() for x in  ItemModel.query.all()]}

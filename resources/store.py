from flask_restful import Resource
from model.store import StoreModel

class Store(Resource):
	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		return {'message': 'store not found '}, 404

	def post(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return {'message': "a store with the name {}, already exist".format(name)}, 400
		store = StoreModel(name)
		try:
			store.add_to_db()
		except:
			return {'message': 'an error occured while adding store'}, 500
		return store.json(), 201

	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()
		return {'message': 'store deleted'}

class StoreList(Resource):
	def get(self):
		return {'items': [x.json() for x in StoreModel.query.all()]}
		




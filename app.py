from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import user_authenticate, identity
from resources.user import UserRegister
from resources.items import Item, Itemlist
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False 
api = Api(app)
app.secret_key = 'hard to crack'

jwt = JWT(app, user_authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores')


if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)


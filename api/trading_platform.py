from flask_restful import Api
from flask import Flask
import sys
import os
import inspect

parent_dir = os.path.dirname(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))))
# This is to make parent folder modules importable
sys.path.insert(0, parent_dir)

# These being imported after addition of new path cause they dependent on module there (db) 
from order import Order
from account import Account

app = Flask(__name__)
api = Api(app)

# This routes can be seperates into more explicit names like /account/create /account/get
# by seperating Resources classes
# kept it this way for the sake of simplicity
api.add_resource(Account, "/account")
api.add_resource(Order, "/order")
if __name__ == "__main__":
    app.run(port=5001)

from flask import Flask, request, jsonify
from service import OrderService, UserService
from models import Schema

import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
   response.headers['Access-Control-Allow-Origin'] = "*"
   response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
   response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
   return response

@app.route("/")
def hello():
   return "Hello World!"


@app.route("/<name>")
def hello_name(name):
   return "Hello " + name

@app.route("/createOrder", methods=["POST"])
def create_order():
   return jsonify(OrderService().create(request.get_json()))

@app.route("/getAll", methods=["GET"])
def list_todo():
   return jsonify(OrderService().list())

@app.route("/updateOrder/<item_id>", methods=["PUT"])
def update_item(item_id):
   return jsonify(OrderService().update(item_id, request.get_json()))

@app.route("/getOrderByID/<item_id>", methods=["GET"])
def get_item(item_id):
   return jsonify(OrderService().get_by_id(item_id))

@app.route("/getOpenOrders", methods=["GET"])
def get_open_item():
   return jsonify(OrderService().get_open_orders())

@app.route("/createUser", methods=["POST"])
def create_user():
   return jsonify(UserService().create(request.get_json()))

@app.route("/listUsers", methods=["GET"])
def list_users():
   return jsonify(UserService().list_users())

@app.route("/deleteUser/<user_id>", methods=["DELETE"])
def delete_user(user_id):
   return jsonify(UserService().delete_user(user_id))


if __name__ == "__main__":
   Schema()
   app.run(debug=True, host='0.0.0.0', port=8000)

from flask import Flask, request, jsonify
from service import CartService
from models import Schema

import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
   response.headers['Access-Control-Allow-Origin'] = "*"
   response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
   response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
   return response

@app.route("/addItemToCart", methods=["POST"])
def add_item():
   return CartService().add_item(request.get_json())

@app.route("/getUserCart/<user_id>", methods=["GET"])
def get_cart(user_id):
   return jsonify(CartService().get_cart(user_id))

@app.route("/removeItemFromCart", methods=["DELETE"])
def remove_item():
   return jsonify(CartService().remove_item(request.get_json()))

@app.route("/deleteCart/<user_id>", methods=["DELETE"])
def delete_cart(user_id):
   return jsonify(CartService().delete_cart(user_id))


if __name__ == "__main__":
   Schema()
   app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask,request,jsonify
from sql_connection import get_sql_connection
import products_dow
import uom_dow
import json
import orders_dow
app = Flask(__name__)

connection = get_sql_connection()#remebmer this one 
@app.route('/getproducts',methods=['GET'])
def get_products():
    products= products_dow.get_all_products(connection)
    response =jsonify(products) #flask need to run this operation very seriously 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/deleteproducts',methods=['POST'])
def delete_products():
    return_id= products_dow.delete_product(connection,request.form['product_id'])#way to supply data from front end to backend
    response =jsonify({
        'product_id':return_id
    }) #flask need to run this operation very seriously 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/getuom',methods=['GET'])
def get_uom():
    products= uom_dow.get_uoms(connection)
    response =jsonify(products) #flask need to run this operation very seriously 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/insertproducts',methods=['POST'])## remember to run server first then depoy
def insert_products():
    #way to supply data from front end to backend
    request_payload = json.loads(request.form['data'])
    product_id= products_dow.insert_new_product(connection,request_payload)
    response =jsonify({
        'product_id':product_id
    }) #flask need to run this operation very seriously 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dow.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dow.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
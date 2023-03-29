from sql_connection import get_sql_connection
def get_all_products(connection):
    cursor = connection.cursor()
    query =("SELECT products.product_id, products.name, products.uom ,products.price_per_unit ,uom.uom_name FROM gs.products inner join gs.uom on products.uom=uom.uom_id ;")
    cursor.execute(query)
    response=[]#storing all values in array
    for (product_id, name, uom ,price_per_unit,uom_name) in cursor:# here is a join donot forget
        response.append(
           {'product_id':product_id,
             'name':name, 
             'uom':uom ,
             'price_per_unit':price_per_unit,
             'uom_name':uom_name
           
           }
        )
    return response


def insert_new_product(connection,product):
    cursor = connection.cursor()
    query =("insert into gs.products"
        "(name,uom,price_per_unit)"
        "values(%s,%s,%s)")
    data =(product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid        #return row id of last row

##def edit_product(connection,product):
  #  cursor = connection.cursor()
    ##query =("UPDATE gs.products"
    ##    "(SET price_per_unit = %s"
      ##  "WHERE product_id= %s")   
    ##data =(product['price_per_unit'],product['product_id'])
    ##cursor.execute(query,data)
   ## connection.commit()
   ## return cursor.lastrowid  

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query =("DELETE FROM products where product_id=" +str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
  
  connection =get_sql_connection()
  print(insert_new_product(connection,{
          'product_name': 'cabbage',
          'uom_id':'1',
          'price_per_unit':'25'}))





  #print(insert_new_product(connection,{
  #         'product_name': 'cabbage',
  #         'uom_id':'1',
  #         'price_per_unit':25}))


  # print(get_all_products(connection))


  # print(delete_product(connection,9)) -- for deletion 
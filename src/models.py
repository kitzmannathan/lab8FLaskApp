import sqlite3

class Schema:
   def __init__(self):
       self.conn = sqlite3.connect('cart.db')
       self.create_user_cart_table()

   def __del__(self):
       # body of destructor
       self.conn.commit()
       self.conn.close()

   def create_user_cart_table(self):
       query = """
       CREATE TABLE IF NOT EXISTS "UserCart" (
       productID INTEGER,
       customerID INTEGER,
       quantity INTEGER,
       PRIMARY KEY (productID, customerID)
       );
       """
       self.conn.execute(query)

class CartModel:
   TABLENAME = "UserCart"

   def __init__(self):
       self.conn = sqlite3.connect('cart.db')
       self.conn.row_factory = sqlite3.Row

   def __del__(self):
       # body of destructor
       self.conn.commit()
       self.conn.close()

   def add_item(self, params):
       query = f'insert into {self.TABLENAME} ' \
               f'(productID, customerID, quantity) ' \
               f'values ("{params.get("productID")}","{params.get("customerID")}","{params.get("quantity")}")'

       result = self.conn.execute(query)
       return "added"

   def get_cart(self, user_id):
       query = f'SELECT * ' \
               f'from {self.TABLENAME} ' \
               f'where customerID = {user_id}'
       result_set = self.conn.execute(query).fetchall()
       print (result_set)
       result = [{column: row[i]
                 for i, column in enumerate(result_set[0].keys())}
                 for row in result_set]
       return result

   def remove_item(self, params):
       query = f'DELETE ' \
               f'from {self.TABLENAME} ' \
               f'WHERE customerID = {params.get("customerID")} AND productID = {params.get("productID")}'
       result = self.conn.execute(query)
       return result

   def delete_cart(self, user_id):
       query = f'DELETE ' \
               f'from {self.TABLENAME} ' \
               f'WHERE customerID = {user_id}'
       result = self.conn.execute(query)
       return "removed"
import sqlite3

class Schema:
   def __init__(self):
       self.conn = sqlite3.connect('lab8.db')
       self.create_user_table()
       self.create_order_table()
       # Why are we calling user table before to_do table
       # what happens if we swap them?

   def __del__(self):
       # body of destructor
       self.conn.commit()
       self.conn.close()

   def create_order_table(self):

       query = """
       CREATE TABLE IF NOT EXISTS "Orders" (
         id INTEGER PRIMARY KEY,
	     items TEXT,
         _is_done boolean DEFAULT 0,
         CreatedOn Date DEFAULT CURRENT_DATE,
         ShipDate Date,
         UserId INTEGER FOREIGNKEY REFERENCES User(_id)
       );
       """

       self.conn.execute(query)

   def create_user_table(self):
       query = """
       CREATE TABLE IF NOT EXISTS "User" (
       _id INTEGER PRIMARY KEY AUTOINCREMENT,
       Name TEXT NOT NULL,
       Email TEXT,
       CreatedOn Date default CURRENT_DATE
       );
       """
       self.conn.execute(query)

class Ordermodel:
   TABLENAME = "Orders"

   def __init__(self):
       self.conn = sqlite3.connect('lab8.db')
       self.conn.row_factory = sqlite3.Row

   def __del__(self):
       # body of destructor
       self.conn.commit()
       self.conn.close()

   def get_by_id(self, _id):
       where_clause = f" WHERE id = {_id}"
       return self.list_items(where_clause)

   def get_open_orders(self):
       where_clause = f" WHERE _is_done = 0"
       return self.list_items(where_clause)

   def create(self, params):
       print (params)
       query = f'insert into {self.TABLENAME} ' \
               f'(Id, Items, CreatedOn, UserId) ' \
               f'values ("{params.get("Id")}","{params.get("Items")}",' \
               f'"{params.get("CreatedOn")}","{params.get("UserId")}")'

       result = self.conn.execute(query)
       return self.get_by_id(result.lastrowid)

   def update(self, item_id, update_dict):
       """
       column: value
       Title: new title
       """
       set_query = ", ".join([f'{column} = "{value}"'
                    for column, value in update_dict.items()])

       query = f"UPDATE {self.TABLENAME} " \
               f"SET {set_query} " \
               f"WHERE id = {item_id}"
       self.conn.execute(query)
       return self.get_by_id(item_id)

   def list_items(self, where_clause=""):
       query = f"SELECT id, items, CreatedOn, ShipDate, _is_done, UserId " \
               f"from {self.TABLENAME}" + where_clause
       result_set = self.conn.execute(query).fetchall()
       print (result_set)
       result = [{column: row[i]
                 for i, column in enumerate(result_set[0].keys())}
                 for row in result_set]
       return result


class UserModel:
   TABLENAME = "User"

   def __init__(self):
       self.conn = sqlite3.connect('lab8.db')
       self.conn.row_factory = sqlite3.Row

   def __del__(self):
       # body of destructor
       self.conn.commit()
       self.conn.close()

   def create(self, params):
       query = f'insert into {self.TABLENAME} ' \
               f'(Name, Email) ' \
               f'values ("{params.get("name")}","{params.get("email")}")'

       result = self.conn.execute(query)
       return self.list_user()

   def list_users(self):
       query = f"SELECT * " \
               f"from {self.TABLENAME}"
       result_set = self.conn.execute(query).fetchall()
       print (result_set)
       result = [{column: row[i]
                 for i, column in enumerate(result_set[0].keys())}
                 for row in result_set]
       return result

   def delete_user(self, user_id):
       query = f"DELETE " \
               f"from {self.TABLENAME} " \
               f"WHERE _id = {user_id}"
       self.conn.execute(query)
       return self.list_users()
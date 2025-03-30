from models import Ordermodel, UserModel


class OrderService:
   def __init__(self):
       self.model = Ordermodel()
   def create(self, params):
       return self.model.create(params)

   def update(self, item_id, params):
       return self.model.update(item_id, params)

   def list(self):
       response = self.model.list_items()
       return response
  
   def get_by_id(self, item_id):
       response = self.model.get_by_id(item_id)
       return response

   def get_open_orders(self):
       response = self.model.get_open_orders()
       return response

class UserService:
    def __init__(self):
        self.model = UserModel()

    def create(self, params):
        return self.model.create(params)

    def list_users(self):
        return self.model.list_users()

    def delete_user(self, user_id):
        return self.model.delete_user(user_id)
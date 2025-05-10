from models import CartModel

class CartService:
    def __init__(self):
        self.model = CartModel()

    def add_item(self, params):
        return self.model.add_item(params)

    def get_cart(self, user_id):
        return self.model.get_cart(user_id)

    def remove_item(self, params):
        return self.model.remove_item(params)

    def delete_cart(self, user_id):
        return self.model.delete_cart(user_id)
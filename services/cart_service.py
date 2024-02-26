from firebase_admin import firestore

db = firestore.client()

class CartService:
    @staticmethod
    def add_item_to_cart(user_id, product_id, quantity):
        """
        Add an item to the user's shopping cart. If the item already exists, update the quantity.
        """
        cart_ref = db.collection('carts').document(user_id)
        cart = cart_ref.get()
        if cart.exists:
            cart_data = cart.to_dict()
            if product_id in cart_data:
                cart_data[product_id] += quantity
            else:
                cart_data[product_id] = quantity
        else:
            cart_data = {product_id: quantity}
        
        cart_ref.set(cart_data)

    @staticmethod
    def remove_item_from_cart(user_id, product_id):
        """
        Remove an item from the user's shopping cart.
        """
        cart_ref = db.collection('carts').document(user_id)
        cart = cart_ref.update({
            product_id: firestore.DELETE_FIELD
        })

    @staticmethod
    def update_item_quantity(user_id, product_id, quantity):
        """
        Update the quantity of an item in the user's shopping cart.
        """
        cart_ref = db.collection('carts').document(user_id)
        cart_ref.update({product_id: quantity})

    @staticmethod
    def get_cart(user_id):
        """
        Retrieve the user's shopping cart.
        """
        cart_ref = db.collection('carts').document(user_id)
        cart = cart_ref.get()
        if cart.exists:
            return cart.to_dict()
        else:
            return {}

    @staticmethod
    def clear_cart(user_id):
        """
        Clear all items from the user's shopping cart.
        """
        db.collection('carts').document(user_id).delete()

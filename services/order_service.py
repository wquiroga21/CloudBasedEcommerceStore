from firebase_admin import firestore
from models.order import Order

db = firestore.client()

class OrderService:
    @staticmethod
    def create_order(user_id, products, total_price):
        """
        Create a new order for the user with the given products and total price.
        """
        order_id = db.collection('orders').document().id  # Generate a unique ID for the order
        order_data = {
            'user_id': user_id,
            'products': products,  # List of tuples (product_id, quantity)
            'total_price': total_price,
            'status': 'pending'  # Default status
        }
        db.collection('orders').document(order_id).set(order_data)
        return order_id

    @staticmethod
    def update_order_status(order_id, status):
        """
        Update the status of an existing order.
        """
        order_ref = db.collection('orders').document(order_id)
        order_ref.update({'status': status})

    @staticmethod
    def get_order(order_id):
        """
        Retrieve a single order by its ID.
        """
        order_ref = db.collection('orders').document(order_id)
        doc = order_ref.get()
        if doc.exists:
            return Order.from_dict(doc.to_dict())
        else:
            return None

    @staticmethod
    def get_user_orders(user_id):
        """
        Retrieve all orders placed by a specific user.
        """
        orders = []
        docs = db.collection('orders').where('user_id', '==', user_id).stream()
        for doc in docs:
            order = Order.from_dict(doc.to_dict())
            orders.append(order)
        return orders

    @staticmethod
    def cancel_order(order_id):
        """
        Cancel an order. This might involve setting the status to 'cancelled' rather than deleting the document.
        """
        order_ref = db.collection('orders').document(order_id)
        order_ref.update({'status': 'cancelled'})

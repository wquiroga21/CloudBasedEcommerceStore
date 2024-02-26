class Order:
    def __init__(self, id, user_id, products, total_price, status="pending"):
        self.id = id
        self.user_id = user_id
        self.products = products  # Expected to be a list of tuples (product_id, quantity)
        self.total_price = total_price
        self.status = status

    def __str__(self):
        return f'Order(id={self.id}, user_id="{self.user_id}", products={self.products}, total_price={self.total_price}, status="{self.status}")'

    def to_dict(self):
        """
        Convert the Order instance into a dictionary format that can be uploaded to Firestore.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'products': self.products,
            'total_price': self.total_price,
            'status': self.status
        }

    @staticmethod
    def from_dict(source):
        """
        Create an Order instance from a dictionary.
        """
        order = Order(id=source['id'], user_id=source['user_id'], products=source['products'],
                      total_price=source['total_price'], status=source.get('status', "pending"))

        return order

# Example usage
if __name__ == '__main__':
    order = Order(id="1", user_id="user_123", products=[("product_456", 2), ("product_789", 1)], total_price=59.97)
    print(order)
    print(order.to_dict())

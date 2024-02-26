class Product:
    def __init__(self, id, name, description, price, stock_quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f'Product(id={self.id}, name="{self.name}", description="{self.description}", price={self.price}, stock_quantity={self.stock_quantity})'

    def to_dict(self):
        """
        Convert the Product instance into a dictionary format that can be uploaded to Firestore.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock_quantity': self.stock_quantity
        }

    @staticmethod
    def from_dict(source):
        """
        Create a Product instance from a dictionary.
        """
        product = Product(id=source['id'], name=source['name'], description=source['description'],
                          price=source['price'], stock_quantity=source['stock_quantity'])

        return product

if __name__ == '__main__':
    product = Product(id="1", name="Sample Product", description="This is a sample product", price=19.99, stock_quantity=100)
    print(product)
    print(product.to_dict())

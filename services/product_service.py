from firebase_admin import firestore
from models.products import Product

db = firestore.client()

class ProductService:
    @staticmethod
    def add_product(product):
        """
        Add a new product to the Firestore database.
        """
        product_ref = db.collection('products').document(product.id)
        product_ref.set(product.to_dict())
        return product.id

    @staticmethod
    def get_product_by_id(product_id):
        """
        Fetch a single product by its ID from Firestore.
        """
        product_ref = db.collection('products').document(product_id)
        doc = product_ref.get()
        if doc.exists:
            return Product.from_dict(doc.to_dict())
        else:
            return None

    @staticmethod
    def update_product(product_id, **kwargs):
        """
        Update product details in Firestore.
        """
        product_ref = db.collection('products').document(product_id)
        product_ref.update(kwargs)

    @staticmethod
    def delete_product(product_id):
        """
        Delete a product from Firestore by its ID.
        """
        db.collection('products').document(product_id).delete()

    @staticmethod
    def list_products():
        """
        List all products in Firestore.
        """
        products = []
        docs = db.collection('products').stream()
        for doc in docs:
            product = Product.from_dict(doc.to_dict())
            products.append(product)
        return products

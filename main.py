# main.py

from config.firebase_config import initialize_firebase
# Initialize Firebase
initialize_firebase()
from models.products import Product
from models.user import User
from services.product_service import ProductService
from services.auth_service import AuthService
from services.cart_service import CartService
from services.order_service import OrderService
from utils.utils import generate_order_id, calculate_total_price, validate_email
import firebase_admin.auth

def main():
    user = User(id="some_unique_id", email="opleasenow.email@email.com", password="password123", name="John Doe", address="123 Elm Street")
    try:
        user_credential = AuthService.create_user(user.email, user.password)
        user_id = user_credential.uid
    except firebase_admin.auth.EmailAlreadyExistsError:
        print(f"An account with the email {user.email} already exists.")
        return

    # Create a new product
    product = Product(id="unique_product_id", name="Product Name", description="Description", price=10.99, stock_quantity=100)
    product_id = ProductService.add_product(product)

    products = ProductService.list_products()
    for product in products:
        print(product)

    # Add the product to the user's shopping cart
    CartService.add_item_to_cart(user_id, product_id, 1)

    # View the user's cart
    cart = CartService.get_cart(user_id)
    print("User's Cart:")
    for product_id in cart:  # Assuming cart contains a list of product IDs
        product = ProductService.get_product_by_id(product_id)  # Fetch product details by ID
        if product:
            # Assuming 'product' is an object with attributes. Adjust if it's a dictionary.
            print(f"Product: {product.name}, Quantity: {product.stock_quantity}")
        else:
            print(f"Product ID {product_id} not found.")


    # Calculate the total price of items in the cart
    total_price = calculate_total_price([product])
    print(f"Total Price: ${total_price}")

    # Create an order for the user
    order_id = generate_order_id(user_id, product_id)
    OrderService.create_order(order_id, user_id, product_id)

    # View the user's orders
    orders = OrderService.get_user_orders(user_id)
    print("User's Orders:")
    for order in orders:
        print(f"Order ID: {order.id}, Products: {order.products}")

if __name__ == "__main__":
    main()
# utils.py

def generate_order_id(user_id, product_id):
    """
    Generate a unique order ID based on the user ID and product ID.
    """
    return f"order_{user_id}_{product_id}"

def calculate_total_price(products):
    """
    Calculate the total price of a list of products.
    """
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price

def validate_email(email):
    """
    Validate if an email address is in a valid format.
    """
    # Simple email validation
    if "@" in email and "." in email:
        return True
    else:
        return False


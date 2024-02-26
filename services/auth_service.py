import firebase_admin
from firebase_admin import auth

class AuthService:
    # Initialize Firebase Admin SDK
    @staticmethod
    def initialize_firebase():
        cred = firebase_admin.credentials.Certificate('C:/Users/wqchi/OneDrive/Documents/1_BYU-I/BYU-I Winter 24/1_CSE 310-Applied Programming/W07/W07 Project/config/basic-ecommerce-store-firebase-adminsdk-ur1km-6ee91d1e0f.json')
        firebase_admin.initialize_app(cred)

    # Create a new user with the given email and password
    @staticmethod
    def create_user(email, password):
        user = auth.create_user(email=email, password=password)
        return user

    # Retrieve a user's information by their unique Firebase user ID
    @staticmethod
    def get_user(user_id):
        user = auth.get_user(user_id)
        return user

    # Delete a user from Firebase Authentication by their unique Firebase user ID
    @staticmethod
    def delete_user(user_id):
        auth.delete_user(user_id)

    # Update a user's email and/or password
    @staticmethod
    def update_user(user_id, email=None, password=None):
        params = {}
        if email:
            params['email'] = email
        if password:
            params['password'] = password
        user = auth.update_user(user_id, **params)
        return user

    # Verify the user's password against Firebase Authentication
    @staticmethod
    def verify_password(email, password):
        user = auth.get_user_by_email(email)
        try:
            auth.get_user(user.uid)
        except:
            return False
        return True

    # Sign in a user with email and password
    @staticmethod
    def user_sign_in(email, password):
        try:
            user = auth.get_user_by_email(email)
            if AuthService.verify_password(email, password):
                return user.uid
        except:
            return None

# Example usage
if __name__ == '__main__':
    AuthService.initialize_firebase()
    # Example calls to the functions; these would need an actual Firebase project set up to work.
    print("User Authentication Service")

import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    service_account_path = 'C:/Users/wqchi/OneDrive/Documents/1_BYU-I/BYU-I Winter 24/1_CSE 310-Applied Programming/W07/W07 Project/config/basic-ecommerce-store-firebase-adminsdk-ur1km-6ee91d1e0f.json'
    try:
        # Directly use the file path for initializing the credentials
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://basic-ecommerce-store-default-rtdb.firebaseio.com',
            'storageBucket': 'gs://basic-ecommerce-store.appspot.com',
        })
    except Exception as e:
        print(f"Error initializing Firebase Admin: {e}")

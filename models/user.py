class User:
    def __init__(self, id, email, password, name="", address=""):
        self.id = id
        self.email = email
        self.password = password  # In a real app, ensure this is hashed
        self.name = name
        self.address = address

    def __str__(self):
        return f'User(id={self.id}, email="{self.email}", name="{self.name}", address="{self.address}")'

    def to_dict(self):
        """
        Convert the User instance into a dictionary format that can be uploaded to Firestore.
        """
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,  # Reminder: Store hashed passwords, not plain text
            'name': self.name,
            'address': self.address
        }

    @staticmethod
    def from_dict(source):
        """
        Create a User instance from a dictionary.
        """
        user = User(id=source['id'], email=source['email'], password=source['password'],
                    name=source.get('name', ""), address=source.get('address', ""))

        return user

# Example usage
if __name__ == '__main__':
    user = User(id="1", email="user@example.com", password="securepassword", name="John Doe", address="123 Elm Street")
    print(user)
    print(user.to_dict())

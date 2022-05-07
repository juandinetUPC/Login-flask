from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname="")->None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname


    # def set_password(self, password):
    #     self.password = generate_password_hash(password)
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

# print(generate_password_hash('1234567'))
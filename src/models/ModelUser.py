from .entities.User import User
class ModelUser():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    @classmethod
    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id, username, password, fullname FROM users WHERE username='{}'".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row:
                user=User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def get_user_by_id(self, db, user_id):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id, username, fullname FROM users WHERE id ={}".format(user_id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row:
                return User(row[0], row[1], None ,row[2])
                
            else: 
                return None
        except Exception as e:
            raise Exception(e)
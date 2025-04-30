class User:
    def __init__(self, username,password):
        self.__username=username
        self.__password=password
        print('konstruktor')
    
    def get__username(self):
        return self.__username
    def get__password(self):
        return self.__password
    def set__username(self,username):
        self.__username=username
    def set__password(self,password):
        self.__password=password
user1= User('Admin','123456')
print(user1.get__password())
user1.set__username('User')
print(user1.get__username())

class Admin(User):
    def __init__(self, username, password,role):
        User.__init__(username,password)
        self.__role=role
        

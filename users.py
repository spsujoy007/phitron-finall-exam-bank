class UserInputs:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email 
        self.address = address

class User(UserInputs):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type

class Admin(UserInputs):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)


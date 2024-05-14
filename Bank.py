# from users import User, Admin
class Bank:
    def __init__(self, name):
        self.name = name
        self.bank_balance = 10000000
        self.users = []
        self.admins = []
        self.loan_amount = 0
        self.loan_activity = False

    # def create_user_account(self, name, email, address, account_type):
    #     user = User(name, email, address, account_type)
    #     self.users.append(user)
    #     return user
    
    # def creatse_admin_account(self):
    #     return Admin()
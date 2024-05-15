# from users import User, Admin
class Bank:
    def __init__(self, name):
        self.name = name
        self.__bank_balance = 10000000
        self.users = []
        self.admins = []
        self.loan_amount = 0
        self.loan_activity = True

    def check_balance(self):
        print(f"\n- Total balance: {self.__bank_balance}tk")
    
    def view_loan_amount(self):
        print(f"\n- Total loan amount is: {self.loan_amount}tk")

    def remove_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print(f"\n- {user.name} is removed.")
                return 
        print("!!! Invalid user account number.")

    def add_user(self, userobject):
        self.users.append(userobject)

    def add_admin(self, adminobject):
        self.admins.append(adminobject)
        print(f"- {adminobject.name} added in admins data.")

    def find_user(self, bank_name, account_number, password):
        for user in bank_name.users:
            if user.account_number == account_number and user.password == password:
                return user
        else:
            return None
        
    def find_admin(self, bank_name, name):
        for admin in bank_name.admins:
            if admin.name == name:
                return True
        else:
            return False
        
    def activate_laonoption(self, option):
        if option == 1:
            self.loan_activity = True
        elif option == 2:
            self.loan_activity = False
        else:
            print("!!! Wrong command")
        
    def view_admins(self):
        print('\n')
        for admin in self.admins:
            print(f"- Admin: {admin.name}, email: {admin.email}, address: {admin.address}")
    
    def view_users(self):
        print('\n')
        for user in self.users:
            print(f"- User: {user.name}, {user.balance}tk, {user.account_type}, {user.account_number}")
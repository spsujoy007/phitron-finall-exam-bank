from datetime import date
from bank import Bank

class UserInputs:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email 
        self.address = address

class History_saver:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount 
        self.date = date.today()

class User(UserInputs):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.account_number = f"{name}{email}"
        self.loan_limit = 2
        self.transition_history = []

   
    def check_balance(self):
        return f"-------------------------------\nYour account balance is: {self.balance}tk\n-------------------------------"

    def deposit(self, amount):
        self.balance += amount
        saveHistory = History_saver('Deposit', amount)
        self.transition_history.append(saveHistory)
        print(f"\n- {amount}tk successfully deposited on your account!")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            saveHistory = History_saver('Withdraw', amount)
            self.transition_history.append(saveHistory)
            print(f"Hey {self.name}! Your {amount}tk  withdrawal was successful.")
        else:
            print("- Withdrawal amount exceeded!!!")
    
    def transfer_money(self, bank_name, amount, account_number):
        if self.balance >= amount:
            for user in bank_name.users:
                if user.account_number == account_number:
                    user.balance += amount
                    self.balance -= amount
                    print(f"- {amount}tk successfully transfered to the account of '{user.name}' ")
                    return
            print("!!! Account does not exist - Transfer failed")
        else:
            print(f"!!! Your transfer amount exceeded")
    
    def take_loan(self, bank_name, amount):
        if bank_name.loan_activity:
            if self.loan_limit > 0:
                self.balance += amount
                bank_name.loan_amount += amount
                self.loan_limit -= 1

                print(f"Congratulations! You got a loan of {amount}tk")
            else:
                print(f"!!! Your withdrawal limit is over")
        else:
            print("!!! Loan activity currently unavailable.")

    def check_transition_history(self):
        for data in self.transition_history:
            print(f'{data.type} | {data.amount}tk in {data.date}')

class Admin(UserInputs):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    
    def remove_user(self, bank_name, account_number):
        for user in bank_name.users:
            if user.account_number == account_number:
                bank_name.users.remove(user)

    def view_users(self, bank_name):
        for user in bank_name.users:
            print(f"info: {user.name}, {user.balance}tk, {user.account_type}, {user.account_number}")

    def view_loan_amount(self, bank_name):
        print(f"Total loan amount is: {bank_name.loan_amount}tk")

    def bank_balance(self, bank):
        print(f"- Total balance: {bank.bank_balance}tk")
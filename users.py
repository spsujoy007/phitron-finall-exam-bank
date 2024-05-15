from datetime import date
# from bank import Bank
import random

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
    def __init__(self, name, email, address, account_type, password):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.password = password
        self.balance = 0
        randomno = random.randint(1, 10000)
        self.account_number = f"{name}{randomno}"
        self.loan_limit = 2
        self.transition_history = []
   
    def check_balance(self):
        return f"\nYour account balance is: {self.balance}tk\n"

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
            print(f"\nHey {self.name}! Your {amount}tk  withdrawal was successful.")
        else:
            print("- Withdrawal amount exceeded!!!")
    
    def transfer_money(self, bank_name, amount, account_number):
        if self.balance >= amount:
            for user in bank_name.users:
                if user.account_number == account_number:
                    user.balance += amount
                    self.balance -= amount
                    saveHistory = History_saver('Transfer money', amount)
                    self.transition_history.append(saveHistory)
                    print(f"- {amount}tk successfully transfered to the account of '{user.name}' ")
                    return
            print("\n!!! Account does not exist - Transfer failed")
        else:
            print(f"\n!!! Your transfer amount exceeded")
    
    def take_loan(self, bank_name, amount):
        if bank_name.loan_activity:
            if self.loan_limit > 0:
                self.balance += amount
                bank_name.loan_amount += amount
                self.loan_limit -= 1
                saveHistory = History_saver('Loan', amount)
                self.transition_history.append(saveHistory)

                print(f"Congratulations! You got a loan of {amount}tk")
            else:
                print(f"!!! Your laon limit is over")
        else:
            print("!!! Loan activity currently unavailable.")

    def check_transition_history(self):
        print("\nTransaction history: ")
        for data in self.transition_history:
            print(f'- {data.type} \t| {data.amount}tk in {data.date}')

class Admin(UserInputs):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
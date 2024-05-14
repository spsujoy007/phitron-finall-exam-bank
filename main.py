from bank import Bank
from users import User, Admin

mamurbank = Bank("Mamur bank")
user = User('rahul', 'emial@.com', 'dhaka', "Saving")
user1 = User('mohon', 'emial@.com', 'dhaka', "Saving")
mamurbank.users.append(user)
mamurbank.users.append(user1)

user.deposit(1000)
user1.deposit(2000)
user.take_loan(mamurbank, 50000)

admin=Admin("Sujoy", "sujoy@gmail.com", 'Dhaka')
admin.bank_balance(mamurbank)
# admin.view_users(mamurbank)
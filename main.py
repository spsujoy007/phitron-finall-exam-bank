from bank import Bank
from users import User, Admin
import os
def clear_terminal():
    os.system('clear')

# bank name
cityBank = Bank("City Bank")

# admin
admin = Admin('Sujoy', "sujoy@gmail.com", 'Dhaka')
cityBank.admins.append(admin)

# Replica start from here...
def UserPanel():
    while(True):
        user = None
        print(f"-----------------------\nWelcome to {cityBank.name}!\n-----------------------")
        print("1. Login\n2. Create account\n3. Exit\n")
        logingcmd = int(input("chose your option: "))
        if logingcmd == 1:
            account_number = input("Enter account number: ")
            password = input("Enter your password: ")
            findUser = cityBank.find_user(cityBank, account_number, password)
            if findUser != None:
                user = findUser
                print(f"Hey {user.name}! Login succesfull.")
            else:
                print("!!! Not a valid user")
                break
        elif logingcmd == 2:
            if user == None:
                username = input("Enter your name: ")
                password = input("Create a password: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                print("\nAccount type: ")
                print("1. Savings\n2. Current")
                type = int(input("CHOSE: "))
                accountType = ''
                if type == 1:
                    accountType = "Savings"
                elif type == 2:
                    accountType = "Current"
                else:
                    accountType = "Savings"
                user = User(username, email, address, accountType, password)
                cityBank.add_user(user)

        elif logingcmd == 3:
             break
        
        if user.name != None:
            print(f"\n\n- Welcome MR/MS {user.name} to the '{cityBank.name}'")
            while(True):
                # clear_terminal()
                print(f"\nYour account number is [{user.account_number}]")
                print("\nOptions:\n-------------------")
                print(f"1. Deposit\n2. Withdraw\n3. Transfer money\n4. Take loan - limit({user.loan_limit})\n5. Check balance\n6. Transaction history\n7. Exit")
                
                cmd = int(input("Chose your option: "))
                if cmd == 1:
                    user.deposit(int(input("Enter amount: ")))
                elif cmd == 2:
                    user.withdraw(int(input("Enter amount: ")))
                elif cmd == 3:
                    user.transfer_money(cityBank, int(input("Enter amount: ")), input("Reciver account number: "))
                elif cmd == 4:
                    user.take_loan(cityBank, int(input("Loan amount: ")))
                elif cmd == 5:
                    print(user.check_balance())
                elif cmd == 6:
                    user.check_transition_history()
                elif cmd == 7:
                    break
                else:
                    print("!!! Wrong command dear")
            

def AdminPanel():
    while(True):
        # clear_terminal()
        print("Chose your option:\n----------------------")
        print("1. Login\n2. Exit\n")
        cmd = int(input("chose your option: "))
        if cmd == 1:
            searchadmin = input("Enter admin name: ")
            if cityBank.find_admin(cityBank, searchadmin):
                while(True):
                    # clear_terminal()
                    print("\nOptions:\n-------------------")
                    print("1. See all user\n2. See all admins\n3. Delete user\n4. Total bank balance\n5. Total loan amount\n6. Loan status\n7. Add admin\n8. Exit")
                    
                    cmd = int(input("chose your option: "))
                    if cmd == 1:
                        cityBank.view_users()
                    elif cmd == 2:
                        cityBank.view_admins()
                    elif cmd == 3:
                        cityBank.remove_user(input("User account number: "))
                    elif cmd == 4:
                        cityBank.check_balance()
                    elif cmd == 5:
                        cityBank.view_loan_amount()
                    elif cmd == 6:
                        print(f"Loan status: {"ON" if cityBank.loan_activity else "NO"}\n")
                        print("Options: \n1. Turn it on \n2. Turn it off\n")
                        choise = int(input("Chose your option: "))
                        cityBank.activate_laonoption(choise)
                    elif cmd == 7:
                        adminname = input("Enter name: ")
                        email = input("Enter email: ")
                        address = input("Enter address: ")
                        admin = Admin(adminname, email, address)
                        cityBank.add_admin(admin)
                    elif cmd == 8:
                        break
            else:
                print("!!! Not a valid admin.")
                break
        else:
            break

while(True):
    clear_terminal()
    print("\nOptions: \n-------------------")
    print("1. User\n2. Admin\n3. Exit\n")
    cmd = int(input("Chose your option: "))
    if cmd == 1:
        UserPanel()
    elif cmd == 2:
        AdminPanel()
    elif cmd == 3:
        break
    else:
        print("!!! Wrong command.")
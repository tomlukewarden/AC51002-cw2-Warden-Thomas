import bank_accounts
import time

def openAccount():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: \n")
    print("Choose an account type: Current Account (A), Savings Account (B), Mortgage Account (C)")
    account_type = input("Enter your desired account type (A, B, C): ")
    
    if account_type == "A":
        print("Opening a current account.")
        print(f"{name} {address} {phone} {email} {account_type}")
    elif account_type == "B":
        print("Opening a savings account.")
        print(f"{name} {address} {phone} {email} {account_type}")
    elif account_type == "C":
        print("Opening a mortgage account.")
        print(f"{name} {address} {phone} {email} {account_type}")
    else:
        print("Invalid account type. Please try again.")
        return openAccount()
    
    print("Account created successfully.")

def existingAccount():
    account_number = int(input("Enter your account number: "))
    account = bank_accounts.get_account_by_number(account_number)  # Assuming a function to retrieve account by number
    if account:
        return account
    else:
        print("Invalid account number. Please try again.")
        return None

def closeAccount():
    account = existingAccount()
    if account:
        close_decision = input("Are you sure you want to close your account? (Y/N): ")
        if close_decision.upper() == "Y":
            account.close()  # Assuming a close method
            print("Account closed successfully.")
        else:
            print("Operation canceled.")

def checkBalance():
    account = existingAccount()
    if account:
        password = input("Please enter your password to check your balance: ")
        if account.verify_password(password):  # Assuming a password verification method
            print(f"Your balance is {account.balance}.")
        else:
            print("Invalid password.")

def deposit():
    account = existingAccount()
    if account:
        amount = float(input("How much would you like to deposit? "))
        account.deposit(amount)  # Assuming deposit method
        print(f"Deposited {amount} successfully.")

def withdraw():
    account = existingAccount()
    if account:
        amount = float(input("How much would you like to withdraw? "))
        if account.withdraw(amount):  # Assuming withdraw method with balance check
            print(f"Withdrew {amount} successfully.")
        else:
            print("Insufficient balance.")
            
def bankingApp():
    print("Welcome to the Python Bank Banking Application! This is a simple banking application. Please select an option from the menu below:")
    time.sleep(1)
    def menu():
        print("\n1. Open a new account")
        print("2. Open an existing account")
        print("3. Close an account")
        print("4. Check balance")
        print("5. Deposit")
        print("6. Withdraw")
        print("7. Exit")
        time.sleep(1)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            openAccount()
            returnToMenu()
        elif choice == "2":
            existingAccount() 
            returnToMenu()
        elif choice == "3":
            closeAccount()
            returnToMenu()
        elif choice == "4":
            checkBalance()
            returnToMenu()
        elif choice == "5":
            deposit()
            returnToMenu()
        elif choice == "6":
            withdraw()
            returnToMenu()
        elif choice == "7":
            print("Exiting the application.")
            exit()
        else:
            print("Invalid input. Please try again.")
            time.sleep(1)
            menu()
    def returnToMenu():
        return_to_menu = input("If you would like to return to our menu? Press enter to continue...")
        if return_to_menu == 'continue':
            print("Returning to menu...")
            time.sleep(1)
            menu()
        else:
            print("Exiting the application.")
            exit()
        returnToMenu()
    menu()
bankingApp()

from bank_accounts import CurrentAccount, SavingAccount, MortgageAccount
import json
from utility import save_to_json, load_from_json
import time

accounts = {}

def openAccount():
    # Get the next available account number
    accounts = load_from_json() # Load accounts from JSON
    if accounts:
        last_account_number = max(accounts.keys()) + 1
    else:
        last_account_number = 1001 
    # Prompt the user for account details
    name = input("Enter your name: ")
    if name == "":
        print("Name cannot be empty. Please try again.")
        return openAccount()
    address = input("Enter your address: ")
    if address == "":
        print("Address cannot be empty. Please try again.")
        return openAccount()
    phone = input("Enter your phone number: ")
    if phone == "":
        print("Phone number cannot be empty. Please try again.")
        return openAccount()
    elif not phone.isdigit():
        print("Phone number must be numeric. Please try again.")
    elif len(phone) != 10:
        print("Phone number must be 10 digits. Please try again.")
        return openAccount()
    email = input("Enter your email: ")
    if email == "":
        print("Email cannot be empty. Please try again.")
        return openAccount()
    elif not email.count("@") == 1:
        print("Email must contain exactly one '@'. Please try again.")
        return openAccount()
    elif not email.count(".") == 1:
        print("Email must contain exactly one '.'. Please try again.")
        return openAccount()
    print("Choose an account type: Current Account (A), Savings Account (B), Mortgage Account (C)")
    account_type = input("Enter your desired account type (A, B, C): ")
    if account_type not in ["A", "B", "C"]:
        print("Invalid account type. Please try again.")
        return openAccount()
    # Create the account based on the user's choice
    if account_type == "A":
        account = CurrentAccount(name, address, phone, email)
        account.account_number = last_account_number
        accounts[account.account_number] = account
        print("Opening a current account.")
        print(account)
    elif account_type == "B":
        account = SavingAccount(name, address, phone, email)
        account.account_number = last_account_number
        accounts[account.account_number] = account
        print("Opening a savings account.")
        print(account)
    elif account_type == "C":
        account = MortgageAccount(name, address, phone, email)
        account.account_number = last_account_number
        accounts[account.account_number] = account
        monthly_repayment = float(input("Enter the monthly repayment amount: "))
        account.monthly_repayment = monthly_repayment
        balance = float(input("Enter the initial balance: "))
        account.balance = -balance
        print("Opening a mortgage account.")
        print(account)
    else:
        # Invalid account type selected
        print("Invalid account type. Please try again.")
        return openAccount()
        
    account.account_number = last_account_number # Assign the next available account number
    accounts[account.account_number] = account # Add the account to the accounts dictionary
    save_to_json(accounts) # Save the accounts dictionary to a JSON file
    print("Account created successfully.")

def checkForAccount(account_number):
    accounts = load_from_json()  # Load accounts from JSON
    if account_number in accounts:
        return True # Account found
    return False

    
def existingAccount():
    accounts = load_from_json()  # Load accounts from JSON
    account_number = int(input("Enter your account number: "))
    if checkForAccount(account_number):
        # Account found 
        print(f"Account found. Welcome back {accounts[account_number].name}!")
        return True
    else:
        print("Account not found. Please check your account number.")
        return False


def existingAccMenu():
    # Existing account menu
    print("\nWelcome to the existing account menu. Please select an option: \n")
    print('1. Check Balance')
    print("2. Deposit")
    print("3. Withdraw")
    print('4. Close Account')
    print("5. Exit App\n")

    choice = input('What would you like to do today? ')

    if choice == "1":
        # Check balance option
        checkBalance()
    elif choice == "2":
        # Deposit option
        deposit()
    elif choice == "3":
        # Withdraw option
        withdraw()
    elif choice == "4":
        # Close account option
        closeAccount()
    elif choice == "5":
        # Exit app option
        exit()

def checkBalance():
    # Check balance option
    accounts = load_from_json()
    account_number = int(input("Please confirm your account number: "))
    if checkForAccount(account_number):
        account = accounts[account_number]
        account.check_balance()
        
    else:
        print("Account not found. Please check your account number.")
    input("Press Enter to return to the menu...")
    existingAccMenu()
    

def deposit():
    accounts = load_from_json() # Load accounts from JSON
    try:
        # Prompt the user for account number and deposit amount
        account_number = int(input("Please confirm your account number: "))
        if account_number in accounts:
            # Account found
            account = accounts[account_number]
            # Prompt the user for deposit amount
            amount = float(input("Enter the amount you would like to deposit: "))
            account.deposit(amount)  
            # Save the accounts dictionary to a JSON file
            save_to_json(accounts)  
        else:
            # Account not found
            print("Account not found. Please check your account number.")
    except ValueError:
        # Invalid input
        print("Invalid input. Please enter numeric values for account number and deposit amount.")
    
    input("Press Enter to return to the menu...\n")
    existingAccMenu()


def withdraw():
    accounts = load_from_json() # Load accounts from JSON

    try:
        # Prompt the user for account number and withdrawal amount
        account_number = int(input("Please confirm your account number: "))
        if account_number in accounts:
            # Account found
            account = accounts[account_number]
            amount = float(input("Enter the amount to withdraw: "))
            # Withdraw the amount from the account
            account.withdraw(amount) 
            # Save the accounts dictionary to a JSON file
            save_to_json(accounts)  
        else:
            # Account not found
            print("Account not found. Please check your account number.\n")
    except ValueError:
        # Invalid input
        print("Invalid input. Please enter numeric values for account number and withdrawal amount.")
    
    input("Press Enter to return to the menu...\n")
    existingAccMenu()

def closeAccount():
    accounts = load_from_json() # Load accounts from JSON

    try:
        # Prompt the user for account number
        account_number = int(input("Please confirm your account number: "))
        if account_number in accounts:
            # Account found
            account = accounts[account_number] 
            account.close_account(accounts)  
            save_to_json(accounts) 
            print("Account closed successfully.\n")
        else:
            # Account not found
            print("Account not found. Please check your account number.")
    except ValueError:
        # Invalid input
        print("Invalid input. Please enter a numeric account number.")
    
    input("Press Enter to return to the menu...\n")
    existingAccMenu()

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
    print('5. Make Payment')
    print("6. Exit App\n")

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
        # Make payment option
        deposit()
    elif choice == "6":
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
    
    input("Press Enter to return to the menu...")
    existingAccMenu()


def withdraw():
    accounts = load_from_json() # Load accounts from JSON

    try:
        # Prompt the user for account number and withdrawal amount
        account_number = int(input("Enter your account number: "))
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
            print("Account not found. Please check your account number.")
    except ValueError:
        # Invalid input
        print("Invalid input. Please enter numeric values for account number and withdrawal amount.")
    
    input("Press Enter to return to the menu...")
    existingAccMenu()

def closeAccount():
    accounts = load_from_json() # Load accounts from JSON

    try:
        # Prompt the user for account number
        account_number = int(input("Confirm your account number: "))
        if account_number in accounts:
            # Account found
            account = accounts[account_number] 
            account.close_account(accounts)  
            save_to_json(accounts) 
            print("Account closed successfully.")
        else:
            # Account not found
            print("Account not found. Please check your account number.")
    except ValueError:
        # Invalid input
        print("Invalid input. Please enter a numeric account number.")
    
    input("Press Enter to return to the menu...")
    existingAccMenu()

def staff_menu():
    # Staff menu
    print("\nWelcome to the staff menu. Please select an option: \n")
    print('1. Show all accounts')
    print("2. Bank Status")
    print('3. Add Interest to all accounts')
    print("4. Exit App\n")

    choice = input('What would you like to do today? (Please leave this field empty and press "ENTER" if you would like to continue as a customer) ')

    if choice == "1":
        # Show all accounts
        all_accounts()
    elif choice == "2":
        # Show ank status
        bank_status()
    elif choice == "3":
        # Add interest to all accounts
        add_interest()
    elif choice == "4":
        # Exit app
        exit()

def all_accounts():
    accounts = load_from_json() # Load accounts from JSON
    print("All accounts:")
    # Display all accounts
    for account_number, account in accounts.items():
        print(f"Account Number: {account_number}")
        print(f"Name: {account.name}")
        print(f"Address: {account.address}")
        print(f"Phone: {account.phone}")
        print(f"Email: {account.email}")
        print(f"Account Type: {account.account_type}")
        print(f"Balance: {account.balance}")
        if isinstance(account, SavingAccount):
            print(f"Interest Rate: {account.interest_rate}")
        elif isinstance(account, MortgageAccount):
            print(f"Interest Rate: {account.interest_rate}")
            print(f"Monthly Repayment: {account.monthly_repayment}\n")
        print("--------------------------------------------------")
        # Print a line to separate each account
    input("Press Enter to return to the menu...")
    staff_menu()
    

def bank_status():
    try:
        accounts = load_from_json() # Load accounts from JSON
        if not isinstance(accounts, list):
            print("Error: 'accounts' is not a list.")
            return

    except FileNotFoundError: # If the file is not found
        print("Error: accounts.json file not found.")
        return
    except json.JSONDecodeError: # If the JSON data cannot be decoded
        print("Error: Failed to decode JSON data.")
        return
    except Exception as e: # For any other unexpected error
        print(f"Unexpected error: {e}")
        return

    # Calculate number of all accounts
    number_of_accounts = len(accounts)
    # Calculate number of each type of account
    number_current_accounts = sum(
        1 for account in accounts if account.get("account_type", "").lower() == "current"
    )
    number_savings_accounts = sum(
        1 for account in accounts if account.get("account_type", "").lower() == "savings"
    )
    number_mortgage_accounts = sum(
        1 for account in accounts if account.get("account_type", "").lower() == "mortgage"
    )
    
    # Calculate total money in savings and current accounts
    total_money = sum(
        account.get("balance", 0) for account in accounts 
        if account.get("account_type", "").lower() in ["current", "savings"]
    )
    
    # Writing bank status to a file
    with open('./files/bank_status.txt', 'w') as bank_status_file:
        bank_status_file.write(f"Total number of accounts: {number_of_accounts}\n")
        bank_status_file.write(f"Number of current accounts: {number_current_accounts}\n")
        bank_status_file.write(f"Number of savings accounts: {number_savings_accounts}\n")
        bank_status_file.write(f"Number of mortgage accounts: {number_mortgage_accounts}\n")
        bank_status_file.write(f"Total money within savings and current accounts: {total_money}\n")
    
    # Display status to the user
    print('Collecting Bank Status, please wait...')
    time.sleep(4)
    print(f"Total number of accounts: {number_of_accounts}")
    print(f"Number of current accounts: {number_current_accounts}")
    print(f"Number of savings accounts: {number_savings_accounts}")
    print(f"Number of mortgage accounts: {number_mortgage_accounts}")
    print(f"Total money within savings and current accounts: {total_money}")
    time.sleep(4)
    staff_menu()

def add_interest():    
    accounts = load_from_json()  # Load accounts from JSON
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    
    for account in accounts.values():
        if isinstance(account, (SavingAccount, MortgageAccount)):  # Check if it's a Saving or Mortgage account
            account.apply_interest()  # Apply interest using the apply_interest method
        elif hasattr(account, "balance"):
            # If it's a regular account (like CurrentAccount), manually add interest
            account.balance += round(account.balance * interest_rate, 2)
            account.balance = round(account.balance, 2)  # Ensure rounding to 2 decimal places
    
    save_to_json(accounts)  # Save the accounts dictionary to the JSON file
    print("Interest added successfully.")
    input("Press Enter to return to the menu...")
    staff_menu()

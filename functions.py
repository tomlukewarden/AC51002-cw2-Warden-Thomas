from bank_accounts import CurrentAccount, SavingAccount, MortgageAccount
from utility import save_to_json, load_from_json

accounts = {}
number_of_accounts = 0
money_all_accounts = 0
number_current_accounts = 0
number_savings_accounts = 0
number_mortgage_accounts = 0

def openAccount():
    global number_of_accounts, number_current_accounts, number_savings_accounts, number_mortgage_accounts, accounts
    try:
        accounts = load_from_json(accounts)
    except FileNotFoundError:
        accounts = {}
    if accounts:
        last_account_number = max(accounts.keys()) + 1
    else:
        last_account_number = 1001 

    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    print("Choose an account type: Current Account (A), Savings Account (B), Mortgage Account (C)")
    account_type = input("Enter your desired account type (A, B, C): ")

    if account_type == "A":
        account = CurrentAccount(name, address, phone, email)
        account.account_number = last_account_number
        accounts[account.account_number] = account
        print("Opening a current account.")
        print(account)
        number_current_accounts += 1
    elif account_type == "B":
        account = SavingAccount(name, address, phone, email)
        account.account_number = last_account_number
        accounts[account.account_number] = account
        print("Opening a savings account.")
        print(account)
        number_savings_accounts += 1
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
        number_mortgage_accounts += 1
    else:
        print("Invalid account type. Please try again.")
        return openAccount()

    # Save the new account number to the file
    with open('./files/last_account_number.txt', 'w') as file:
        file.write(str(last_account_number + 1))  
        
    save_to_json(accounts)
    number_of_accounts += 1
    print("Account created successfully.")

def checkForAccount(account_number):
    global accounts
    load_from_json(accounts)  # Load existing accounts from JSON
    if account_number in accounts:
        return True
    else:
        return False

def existingAccount():
    global accounts

    account_number = int(input("Enter your account number: "))
    # Pass the account number to checkForAccount and directly return True or False
    if checkForAccount(account_number):
        print(f"Account found. Welcome back {accounts[account_number].name}!")
        return True
    else:
        print("Account not found. Please check your account number.")
        return False

def existingAccMenu():
    print("\nWelcome to the existing account menu. Please select an option: \n")
    print('1. Check Balance')
    print("2. Deposit")
    print("3. Withdraw")
    print('4. Close Account')
    print("5. Exit App\n")

    choice = input('What would you like to do today? ')

    if choice == "1":
        checkBalance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        closeAccount()
    elif choice == "5":
        exit()

def checkBalance():
    account_number = int(input("Please confirm your account number: "))
    if checkForAccount(account_number):
        print(accounts[account_number].balance)
    else:
        print("Account not found. Please check your account number.")
    input("Press Enter to return to the menu...")
    existingAccMenu()

def deposit():
    account_number = int(input("Enter your account number: "))
    if checkForAccount(account_number):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            accounts[account_number].balance += amount  # Update balance directly
            save_to_json(accounts)  # Save the updated accounts dictionary
            print(f"Deposit successful. New balance: {accounts[account_number].balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    else:
        print("Account not found. Please check your account number.")
    input("Press Enter to return to the menu...")
    existingAccMenu()

def withdraw():
    account_number = int(input("Enter your account number: "))
    if checkForAccount(account_number):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and accounts[account_number].balance >= amount:
            accounts[account_number].balance -= amount  # Update balance directly
            save_to_json(accounts)  # Save the updated accounts dictionary
            print(f"Withdrawal successful. New balance: {accounts[account_number].balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    else:
        print("Account not found. Please check your account number.")
    input("Press Enter to return to the menu...")
    existingAccMenu()
    
def closeAccount():
    account_number = int(input("Confirm your account number: "))
    if checkForAccount(account_number):
        del accounts[account_number]
        save_to_json(accounts)  # Save the updated accounts dictionary
        print("Account closed successfully.")
    else:
        print("Account not found. Please check your account number.")
    input("Press Enter to return to the menu...")
    existingAccMenu()
            
def staff_menu():
    print("\nWelcome to the staff menu. Please select an option: \n")
    print('1. Show all accounts')
    print("2. Bank Status")
    print('3. Add Interest to all accounts')
    print("4. Exit App\n")

    choice = input('What would you like to do today? ')

    if choice == "1":
        all_accounts()
    elif choice == "2":
        bank_status()
    elif choice == "3":
        add_interest()
    elif choice == "4":
        exit()

def all_accounts():
    load_from_json(accounts)
    print("All accounts:")
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
            print(f"Monthly Repayment: {account.monthly_repayment}/n")
        print("--------------------------------------------------")
    input("Press Enter to return to the menu...")
    staff_menu()
def bank_status():
    load_from_json(accounts)
    number_of_accounts = len(accounts)
    
    with open('./files/bank_status.txt', 'a'):
        print("Bank Status:")
        print(f"Number of accounts: {number_of_accounts}")
        print(f"Number of current accounts: {number_current_accounts}")
        print(f"Number of savings accounts: {number_savings_accounts}")
        print(f"Number of mortgage accounts: {number_mortgage_accounts}")
        print(f"Total balance: {money_all_accounts}")
        print("--------------------------------------------------")
        input("Press Enter to return to the menu...")
        staff_menu()

def add_interest():
    load_from_json(accounts)  # Load accounts from JSON file
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100

    for account in accounts.values():  # Iterate through account objects
        if hasattr(account, "balance"):  # Ensure the account has a balance attribute
            account.balance += round(account.balance * interest_rate, 2)  # Apply interest
    save_to_json(accounts)  # Save updated accounts back to JSON
    print("Interest added successfully.")
    input("Press Enter to return to the menu...")
    staff_menu()


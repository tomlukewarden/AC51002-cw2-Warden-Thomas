import bank_accounts

from utility import save_to_json, load_from_json
accounts = {}
number_of_accounts = 0
money_all_accounts = 0
number_current_accounts = 0
number_savings_accounts = 0
number_mortgage_accounts = 0

def openAccount():
    global number_of_accounts, number_current_accounts, number_savings_accounts, number_mortgage_accounts

    # Read the last account number
    try:
        with open('./files/last_account_number.txt', 'r') as file:
            last_account_number = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        last_account_number = 1001  # Default starting value if the file doesn't exist or is invalid

    # Create account details
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    print("Choose an account type: Current Account (A), Savings Account (B), Mortgage Account (C)")
    account_type = input("Enter your desired account type (A, B, C): ")

    if account_type == "A":
            account = bank_accounts.CurrentAccount(name, address, phone, email)
            account.account_number = last_account_number  
            accounts[account.account_number] = account
            print("Opening a current account.")
            print(account)
            number_current_accounts += 1
    elif account_type == "B":
            account = bank_accounts.SavingAccount(name, address, phone, email)
            account.account_number = last_account_number
            accounts[account.account_number] = account
            print("Opening a savings account.")
            print(account)
            number_savings_accounts += 1
    elif account_type == "C":
            account = bank_accounts.MortgageAccount(name, address, phone, email)
            account.account_number = last_account_number
            accounts[account.account_number] = account
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
    if existingAccount():
        choice = input("Are you sure you want to close your account? (yes/no): ")
        if choice.lower() == "yes":
            account_number = int(input("Enter your account number: "))
            if checkForAccount(account_number):
                del accounts[account_number]
                save_to_json(accounts)
            print("Account closed successfully.")

def all_accounts():
    with open ("./files/all_accounts.txt", "r") as accounts:
        print("Open Accounts:")
        print(accounts.read())
        
def bank_status():
    
    with open ("./files/bank_stat.txt", "w") as bank_status:
        bank_status.write(f"Number of accounts: {number_of_accounts}\n")
        bank_status.write(f"Number of current accounts: {number_current_accounts}\n")
        bank_status.write(f"Number of savings accounts: {number_savings_accounts}\n")
        bank_status.write(f"Number of mortgage accounts: {number_mortgage_accounts}\n")
        bank_status.write(f"Total money in all accounts: {money_all_accounts}\n")
    print("Current Bank Status:")
    print(f"Number of accounts: {number_of_accounts}")
    print(f"Number of current accounts: {number_current_accounts}")
    print(f"Number of savings accounts: {number_savings_accounts}")
    print(f"Number of mortgage accounts: {number_mortgage_accounts}")
    print(f"Total money in all accounts: {money_all_accounts}")

import bank_accounts
import time

accounts = {}
number_of_accounts = 0
money_all_accounts = 0
number_current_accounts = 0
number_savings_accounts = 0
number_mortgage_accounts = 0

def openAccount():
    global number_of_accounts, number_current_accounts, number_savings_accounts, number_mortgage_accounts

    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    print("Choose an account type: Current Account (A), Savings Account (B), Mortgage Account (C)")
    account_type = input("Enter your desired account type (A, B, C): ")

    file_path = "./files/accounts.txt"
    with open(file_path, "a") as accounts_file:
        if account_type == "A":
            account = bank_accounts.CurrentAccount(name, address, phone, email)
            accounts[account.account_number] = account
            print("Opening a current account.")
            accounts_file.write(str(account) + "\n")
            print(account)
            number_of_accounts += 1
            number_current_accounts += 1
        elif account_type == "B":
            account = bank_accounts.SavingAccount(name, address, phone, email)
            accounts[account.account_number] = account
            print("Opening a savings account.")
            accounts_file.write(str(account) + "\n")
            print(account)
            number_of_accounts += 1
            number_savings_accounts += 1
        elif account_type == "C":
            account = bank_accounts.MortgageAccount(name, address, phone, email)
            accounts[account.account_number] = account
            print("Opening a mortgage account.")
            accounts_file.write(str(account) + "\n")
            print(account)
            number_of_accounts += 1
            number_mortgage_accounts += 1
        else:
            print("Invalid account type. Please try again.")
            return openAccount()

    print("Account created successfully.")

def existingAccount():
    accounts = {}
    with open('./files/accounts.txt', 'r') as accounts_file:
        lines = [line.strip() for line in accounts_file if line.strip()] 
        
        for i in range(0, len(lines), 4):
            account_number_line = lines[i + 2]  
            if "Account number:" in account_number_line:
                account_number = int(account_number_line.split(":")[1].strip())
                accounts[account_number] = True

    try:
        account_number = int(input("Enter your account number: "))
    except ValueError:
        print("Invalid input. Please enter a valid account number.")
        return None

    if accounts.get(account_number):
        print("Account found.")
        return True
    else:
        print("Invalid account number. Please try again.")
        return False
    
def existingAccMenu():
    choice = input('What would you like to do today?')
    print('1. Check Balance')
    print("2. Deposit")
    print("3. Withdraw")
    print('4. Close Account')
    print("5. Return to First Menu")

    if choice == "1":
        checkBalance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        closeAccount()
    elif choice == "5":
        bankingApp()

def closeAccount():
    account = existingAccount()
    if account:
        close_decision = input("Are you sure you want to close your account? (Y/N): ")
        if close_decision.upper() == "Y":
            del accounts[account.account_number]
            print("Account closed successfully.")
        else:
            print("Operation canceled.")

def checkBalance():
    account = existingAccount()
    if account:
        account.check_balance()

def deposit():
    global money_all_accounts
    account = existingAccount()
    if account:
        amount = float(input("How much would you like to deposit? "))
        account.deposit(amount)
        money_all_accounts += amount

def withdraw():
    global money_all_accounts
    account = existingAccount()
    if account:
        amount = float(input("How much would you like to withdraw? "))
        account.withdraw(amount)
        money_all_accounts -= amount

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

def bankingApp():
    print("Welcome to the Python Bank Banking Application!")
    time.sleep(1)

    while True:
        print("\n1. Open a new account")
        print("2. Open an existing account")
        print("3. Close an account")
        print("4. Check balance")
        print("5. Deposit")
        print("6. Withdraw")
        print("7. Show state of all accounts")
        print("8. Bank Status")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            openAccount()
        elif choice == "2":
            existingAccount()
            if existingAccount():
                existingAccMenu()

        elif choice == "3":
            closeAccount()
        elif choice == "4":
            checkBalance()
        elif choice == "5":
            deposit()
        elif choice == "6":
            withdraw()
        elif choice == "7":
            print("All accounts state:")
            if accounts:
                account_numbers = list(accounts.keys())
                for account_number in account_numbers:
                    print(f'Account Number: {account_number}, Status: OPEN\n')
            else:
                print("No accounts available.")
        elif choice == "8":
            bank_status()
        elif choice == "9":
            print("Exiting the application.")
            break
        else:
            print("Invalid input. Please try again.")
        
        input("Press Enter to return to the menu...")

bankingApp()

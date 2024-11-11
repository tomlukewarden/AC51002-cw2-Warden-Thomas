import bank_accounts
import time

accounts = {}  

def openAccount():
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
        elif account_type == "B":
            account = bank_accounts.SavingAccount(name, address, phone, email)
            accounts[account.account_number] = account
            print("Opening a savings account.")
            accounts_file.write(str(account) + "\n")
            print(account)
        elif account_type == "C":
            account = bank_accounts.MortgageAccount(name, address, phone, email)
            accounts[account.account_number] = account
            print("Opening a mortgage account.")
            accounts_file.write(str(account) + "\n")
            print(account)
        else:
            print("Invalid account type. Please try again.")
            return openAccount()
    
    print("Account created successfully.")

def existingAccount():
    
    account_number = int(input("Enter your account number: "))
    account = accounts.get(account_number)
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
            del accounts[account.account_number]
            print("Account closed successfully.")
        else:
            print("Operation canceled.")

def checkBalance():
    account = existingAccount()
    if account:
        account.check_balance()

def deposit():
    account = existingAccount()
    if account:
        amount = float(input("How much would you like to deposit? "))
        account.deposit(amount)

def withdraw():
    account = existingAccount()
    if account:
        amount = float(input("How much would you like to withdraw? "))
        account.withdraw(amount)
            
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
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            openAccount()
        elif choice == "2":
            existingAccount() 
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
                for account_number, account in accounts.items():
                    print(f'Account Number: {account_number}, Status: OPEN')
            else:
                print("No accounts available.")
        elif choice == "8":
            print("Exiting the application.")
            exit()
        else:
            print("Invalid input. Please try again.")
        
        input("Press Enter to return to the menu...")

bankingApp()    
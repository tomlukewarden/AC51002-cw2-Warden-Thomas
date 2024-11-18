import bank_accounts
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

    file_path = "./files/all_accounts.txt"
    with open(file_path, "a") as accounts_file, open(f'./files/account_type/{account_type.lower()}.txt', 'a') as current:
        if account_type == "A":
            account = bank_accounts.CurrentAccount(name, address, phone, email)
            account.account_number = last_account_number  
            accounts[account.account_number] = account
            print("Opening a current account.")
            accounts_file.write(str(account) + "\n")
            current.write(str(account) + "\n")
            print(account)
            number_current_accounts += 1
        elif account_type == "B":
            account = bank_accounts.SavingAccount(name, address, phone, email)
            account.account_number = last_account_number
            accounts[account.account_number] = account
            print("Opening a savings account.")
            accounts_file.write(str(account) + "\n")
            print(account)
            number_savings_accounts += 1
        elif account_type == "C":
            account = bank_accounts.MortgageAccount(name, address, phone, email)
            account.account_number = last_account_number
            accounts[account.account_number] = account
            print("Opening a mortgage account.")
            accounts_file.write(str(account) + "\n")
            print(account)
            number_mortgage_accounts += 1
        else:
            print("Invalid account type. Please try again.")
            return openAccount()

    # Save the new account number to the file
    with open('./files/last_account_number.txt', 'w') as file:
        file.write(str(last_account_number + 1))  

    number_of_accounts += 1
    print("Account created successfully.")

def checkForAccount():
    global accounts, number_of_accounts
    try:
        with open('./files/all_accounts.txt', 'r') as accounts_file:
            lines = [line.rstrip() for line in accounts_file]
            for i in range(0, len(lines), 6):
                try:
                    account_number_line = lines[i + 3]  
                    if "Account number:" in account_number_line:
                        account_number = int(account_number_line.split(":")[1].strip())
                        accounts[account_number] = True
                        number_of_accounts += 1  # Keep track of the number of accounts
                except (IndexError, ValueError):
                    print(f"Error processing account at lines {i} to {i+5}. Skipping.")
    except FileNotFoundError:
        print("Error: File './files/all_accounts.txt' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return accounts

def existingAccount():
    global accounts

    account_number = int(input("Enter your account number: "))
    if account_number in checkForAccount():
        print("Account found. Welcome back!")
        return True
    else:
        print("Account not found. Please check your account number.")
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


def closeAccount():
    if existingAccount():
        choice = input("Are you sure you want to close your account? (yes/no): ")
        if choice.lower() == "yes":
            account_number = int(input("Enter your account number: "))
            with open('./files/all_accounts.txt', 'r') as accounts_file:
                lines = accounts_file.readlines()
            with open('./files/all_accounts.txt', 'w') as accounts_file:
                for line in lines:
                    if f"Account number: {account_number}" not in line:
                        accounts_file.write(line)
            print("Account closed successfully.")

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

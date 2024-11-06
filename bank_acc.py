import bank_accounts
import time

# Set up menu

def bankingApp():

    print("Welcome to the banking application. Please select an option from the menu below:")
    time.sleep(1)
    while True:
        print("1. Open a new account")
        print("2. Open an existing account")
        print("3. Close an account")
        print("4. Check balance")
        print("5. Deposit")
        print("6. Withdraw")
        print("7. Exit")
        time.sleep(1)
        choice = input("Enter your choice: ")
    
        if choice == "1":
            def openAccount():
                name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone = input("Enter your phone number: ")
                email = input("Enter your email: \n")
                print("Choose an account type, Current Account (A), Savings Account (B), Mortgage Account (C): ")
                account_type = input("Enter your desired account type (A, B, C): ")
                
                if account_type == "A":
                    account_type = bank_accounts.CurrentAccount
                elif account_type == "B":
                    account_type = bank_accounts.SavingAccount
                elif account_type == "C":
                    account_type = bank_accounts.MortgageAccount
                else:
                    print("Invalid account type. Please try again.")
                    openAccount()
        elif choice == "2":
            def existingAccount():
                account_number_check = int(input("Enter your account number: "))
                if account_number_check in bank_accounts.account_number:
                    print("Opening account...")
                else:
                    print("Invalid account number. Please try again.")
                existingAccount()
        elif choice == "3":
            existingAccount()
            close_decision = input("Are you sure you want to close your account? (Y/N): ")
            if close_decision == "Y":
                print("Closing account...")
            elif close_decision == "N":
                print("Exiting...")
            else:
                print("Invalid input. Exiting...")
        elif choice == "4":
            existingAccount()
            balance_check = input("Please enter your password to check your balance: ")
            if balance_check == bank_accounts.password:
                print(f'Your balance is {bank_accounts.balance}.')
            else:
                print("Invalid password. Please try again.")
        elif choice == "5":
            existingAccount()
            deposit_decision = int(input("How much would you want to deposit? (Enter a number): "))
            print('Deposit amount:', deposit_decision)
            deposit_decision = bank_accounts.deposit(deposit_decision)
        elif choice == "6":
            existingAccount()
            withdraw_decision = int(input("How much would you want to withdraw? (Enter a number): "))
            print('Withdraw amount:', withdraw_decision)
            withdraw_decision = bank_accounts.withdraw(withdraw_decision)
        elif choice == "7":
            print('Exiting')
        else:
            print('Invalid input')
            time.sleep(1)
bankingApp()
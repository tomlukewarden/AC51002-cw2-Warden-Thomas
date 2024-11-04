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
            print('Opening new account')
        elif choice == "2":
            print('Opening your account')
        elif choice == "3":
            print('Closing your account')
        elif choice == "4":
            print('Checking balance')
        elif choice == "5":
            print('Depositing')
        elif choice == "6":
            print('Withdrawing')
        elif choice == "7":
            print('Exiting')
        else:
            print('Invalid input')
            time.sleep(1)
bankingApp()
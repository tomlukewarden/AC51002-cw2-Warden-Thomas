
from functions import openAccount, existingAccount,existingAccMenu, bank_status, all_accounts, staff_menu
import time

def staff():
    is_staff = input("If you are a staff member please enter the password:")
    if is_staff == "password":
        staff_menu()
    elif is_staff != "password":
        print("Wrong password, please continue as a customer")
    else:
        print("Invalid input. Please try again.")
        exit()
staff()

def bankingApp():
    print("Welcome to the Python Bank Banking Application!")
    time.sleep(1)

    while True:
        print("\n1. Open a new account")
        print("2. Open an existing account")
        print("3. Show state of all accounts")
        print("4. Bank Status")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            openAccount()
        elif choice == "2":
            account = existingAccount()
            if account:
                existingAccMenu()
        elif choice == "3":
            all_accounts()
        elif choice == "4":
            bank_status()
        elif choice == "5":
            print("Thank you for using the Python Bank Banking Application!")
            exit()
        else:
            print("Invalid input. Please try again.")
        
        input("Press Enter to return to the menu...")
bankingApp()
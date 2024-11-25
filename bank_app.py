
from functions import openAccount, existingAccount,existingAccMenu, staff_menu
import time

def staff():
    is_staff = input("If you are a staff member please enter the password, please press 'ENTER' and continue as a customer: ")
    if is_staff == "password":
        staff_menu()
    elif is_staff == "":
        pass
    elif is_staff != "password":
        print("Wrong password, try again")
        staff()
    else:
        print("Invalid input. Please try again.")
        staff()
staff()
def bankingApp():
    print("Welcome to the Python Bank Banking Application!")
    time.sleep(1)

    while True:
        print("\n1. Open a new account")
        print("2. Open an existing account")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            openAccount()
        elif choice == "2":
            account = existingAccount()
            if account:
                existingAccMenu()
        elif choice == "3":
            print("Thank you for using the Python Bank Banking Application!")
            exit()
        else:
            print("Invalid input. Please try again.")
        
        input("Press Enter to return to the menu...")
bankingApp()
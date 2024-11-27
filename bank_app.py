'''
Bringing functions through for the banking app
Doing this is separate files makes the readability of the code better
'''
from customer_functions import openAccount, existingAccount,existingAccMenu
from staff_functions import staff_menu
import time

def staff():
    # Check if user is staff
    
    is_staff = input("If you are a staff member please enter the password, please press 'ENTER' and continue as a customer: ")
    if is_staff == "password":
        # Call staff menu if user gets password correct
        staff_menu()
    elif is_staff == "":
        # If the user  leaves this field empty, assume they are a customer and continue to the banking app
        pass
    elif is_staff != "password":
        print("Wrong password, try again")
        # If the user enters the wrong password, ask them to try again
        staff()
    else:
        # If the user enters something else, assume they are a customer and continue to the banking app
        print("Invalid input. Please try again.")
        staff()
staff()
def bankingApp():
    print("Welcome to the Python Bank Banking Application!")
    time.sleep(1)

    # Main menu - Smaller than the existing account menu
    while True:
        print("\n1. Open a new account")
        print("2. Open an existing account")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            openAccount() # Function to open an account
        elif choice == "2":
            account = existingAccount() # Function to open an existing account
            if account:
                existingAccMenu() # Function to open the existing account menu
        elif choice == "3":
            print("Thank you for using the Python Bank Banking Application!") 
            # Exit the program
            exit()
        else:
            print("Invalid input. Please try again.")
        input("Press Enter to return to the menu...")
bankingApp()
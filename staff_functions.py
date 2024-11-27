import json
import time
from bank_accounts import SavingAccount, MortgageAccount
from utility import save_to_json, load_from_json
def staff_menu():
    # Staff menu
    print("\nWelcome to the staff menu. Please select an option: \n")
    print('1. Show all accounts')
    print("2. Bank Status")
    print('3. Add Interest to all accounts')
    print("4. Exit App\n")

    choice = input('What would you like to do today? (Please leave this field empty and press "ENTER" if you would like to continue as a customer) ')

    if choice == "1":
        # Show all accounts
        all_accounts()
    elif choice == "2":
        # Show bank status
        bank_status()
    elif choice == "3":
        # Add interest to all accounts
        add_interest()
    elif choice == "4":
        # Exit app
        exit()

def all_accounts():
    accounts = load_from_json() # Load accounts from JSON
    print("Fetching all accounts\n")
    time.sleep(2)
    print("All accounts:")
    # Display all accounts
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
            print(f"Monthly Repayment: {account.monthly_repayment}\n")
        print("--------------------------------------------------")
        # Print a line to separate each account
        time.sleep(2)
    input("Press Enter to return to the menu...")
    staff_menu()
    
def bank_status():
    try:
        accounts = load_from_json()  # This returns a dictionary of account objects
    except FileNotFoundError:
        print("Error: accounts.json file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    
    # Initialize counts and total money
    number_of_accounts = len(accounts)
    number_current_accounts = 0
    number_savings_accounts = 0
    number_mortgage_accounts = 0
    total_money = 0

    # Iterate over each account in the dictionary
    for account in accounts.values():
        account_type = account.__class__.__name__  # Get the type of the account from the class name
        
        # Count the types of accounts
        if account_type == "CurrentAccount":
            number_current_accounts += 1
        elif account_type == "SavingAccount":
            number_savings_accounts += 1
        elif account_type == "MortgageAccount":
            number_mortgage_accounts += 1
        
        # Add the balance of current and savings accounts to the total money
        if account_type in ["CurrentAccount", "SavingAccount"]:
            total_money += account.balance

    # Writing bank status to a file
    with open('./files/bank_status.txt', 'w') as bank_status_file:
        bank_status_file.write(f"Total number of accounts: {number_of_accounts}\n")
        bank_status_file.write(f"Number of current accounts: {number_current_accounts}\n")
        bank_status_file.write(f"Number of savings accounts: {number_savings_accounts}\n")
        bank_status_file.write(f"Number of mortgage accounts: {number_mortgage_accounts}\n")
        bank_status_file.write(f"Total money within savings and current accounts: {total_money}\n")

    # Display status to the user
    print('Collecting Bank Status, please wait...')
    time.sleep(4)
    print(f"Total number of accounts: {number_of_accounts}")
    print(f"Number of current accounts: {number_current_accounts}")
    print(f"Number of savings accounts: {number_savings_accounts}")
    print(f"Number of mortgage accounts: {number_mortgage_accounts}")
    print(f"Total money within savings and current accounts: {total_money}")
    time.sleep(4)

    staff_menu()

def add_interest():    
    accounts = load_from_json()  # Load accounts from JSON
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    for account in accounts.values():
        if isinstance(account, (SavingAccount, MortgageAccount)):  # Check if it's a Saving or Mortgage account
            account.apply_interest()  # Apply interest using the apply_interest method
        elif hasattr(account, "balance"):
            # If it's a regular account (like CurrentAccount), manually add interest
            account.balance += round(account.balance * interest_rate, 2)
            account.balance = round(account.balance, 2)  # Ensure rounding to 2 decimal places
    
    save_to_json(accounts)  # Save the accounts dictionary to the JSON file
    print("Interest added successfully.")
    input("Press Enter to return to the menu...")
    staff_menu()

import json
from bank_accounts import CurrentAccount, SavingAccount, MortgageAccount

def save_to_json(accounts, filename='accounts.json'):
    # Convert accounts to a list of dictionaries
    data = [
        {
            "account_number": account.account_number,
            "name": account.name,
            "address": account.address,
            "phone": account.phone,
            "email": account.email,
            "account_type": account.account_type,
            "balance": account.balance,
            # Add interest rate using the created class
            **({"interest_rate": account.interest_rate} if isinstance(account, SavingAccount) else {}), 
            # Add interest rate and monthly repayment using the created class
            **({"interest_rate": account.interest_rate, "monthly_repayment": account.monthly_repayment} 
            if isinstance(account, MortgageAccount) else {})
        }
        for account in accounts.values()
    ]
    try:
        # Write the data to the JSON file
        with open(filename, 'w') as file:
            # Use json.dump to write the data to the file
            json.dump({"accounts": data}, file, indent=4)
            # Use indent=4 to make the JSON file more readable
        print(f"Accounts saved successfully to {filename}.")
        # If the file is successfully written, print this success message
    except Exception as e:
        # If there is an error, print this error message
        print(f"Error saving accounts to {filename}: {e}")


def load_from_json(filename='accounts.json'):
    accounts = {}
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data.get("accounts", []):
                if item["account_type"] == "Current":
                    account = CurrentAccount(
                        item["name"], item["address"], item["phone"], item["email"]
                    )
                elif item["account_type"] == "Savings":
                    account = SavingAccount(
                        item["name"], item["address"], item["phone"], item["email"]
                    )
                    account.interest_rate = item.get("interest_rate", 0.0)
                elif item["account_type"] == "Mortgage":
                    account = MortgageAccount(
                        item["name"], item["address"], item["phone"], item["email"]
                    )
                    account.interest_rate = item.get("interest_rate", 0.0)
                    account.monthly_repayment = item.get("monthly_repayment", 0.0)

                account.account_number = item["account_number"]
                account.balance = item["balance"]
                accounts[account.account_number] = account

    except FileNotFoundError:
        print(f"No file named {filename} found. Starting with an empty accounts database.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON file {filename}. Ensure it is properly formatted.")
    except KeyError as e:
        print(f"Missing key in JSON data: {e}")
    except Exception as e:
        print(f"Unexpected error while loading accounts: {e}")

    return accounts

import json
from bank_accounts import CurrentAccount, SavingAccount, MortgageAccount

def save_to_json(accounts, filename='accounts.json'):
    data = [
        {
            "account_number": account.account_number,
            "name": account.name,
            "address": account.address,
            "phone": account.phone,
            "email": account.email,
            "account_type": account.account_type,
            "balance": account.balance,
            **({"interest_rate": account.interest_rate} if isinstance(account, SavingAccount) else {}),
            **({"interest_rate": account.interest_rate, "monthly_repayment": account.monthly_repayment} 
               if isinstance(account, MortgageAccount) else {})
        }
        for account in accounts.values()
    ]
    with open(filename, 'w') as file:  
        json.dump({"accounts": data}, file, indent=4)
    print(f"Accounts saved to {filename}.")

def load_from_json(accounts, filename='accounts.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data["accounts"]:
                if item["account_number"] not in accounts:  # Avoid duplicating existing accounts
                    if item["account_type"] == "Current":
                        account = CurrentAccount(item["name"], item["address"], item["phone"], item["email"], item["balance"])
                    elif item["account_type"] == "Savings":
                        account = SavingAccount(item["name"], item["address"], item["phone"], item["email"], item["balance"], item["interest_rate"])
                    elif item["account_type"] == "Mortgage":
                        account = MortgageAccount(item["name"], item["address"], item["phone"], item["email"], item["balance"], item["interest_rate"], item["monthly_repayment"])
                    account.account_number = item["account_number"]
                    accounts[account.account_number] = account
    except FileNotFoundError:
        print(f"No file named {filename} found.")
        return accounts  # Return the existing dictionary, even if it's empty
    return accounts

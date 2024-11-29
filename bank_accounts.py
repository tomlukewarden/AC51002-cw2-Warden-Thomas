# CustomerDetails class
class CustomerDetails:
    last_account_number = 1001

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    @classmethod
    # Generate and return the next available account number
    def generate_account_number(cls):
        account_number = cls.last_account_number
        cls.last_account_number += 1
        return account_number

# CurrentAccount class
class CurrentAccount(CustomerDetails): # Inherit from CustomerDetails
    def __init__(self, name, address, phone, email, balance=0):
        super().__init__(name, address, phone, email) # Call the constructor of the parent class
        self.account_number = CustomerDetails.generate_account_number() # Generate and assign the account number
        self.account_type = "Current"
        self.balance = round(balance, 2) # Round the balance

    def deposit(self, amount):
        if amount > 0: # Check if the deposit amount is positive
            self.balance += amount
            self.balance = round(self.balance, 2) # Round the balance
            print(f"Deposit successful. New balance: {self.balance}\n") # Print the updated balance
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount: # Check if the withdrawal amount is positive and there is enough balance
            self.balance -= amount
            self.balance = round(self.balance, 2) # Round the balance
            print(f"Withdrawal successful. New balance: {self.balance}\n") # Print the updated balance
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def check_balance(self):
        # Check and print the current balance
        print(f"Current balance: {self.balance}\n")

    def close_account(self, accounts_dict):
        # Remove the account from the dictionary
        del accounts_dict[self.account_number]
        print("Account closed successfully.\n")

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "account_number": self.account_number,
            "account_type": self.account_type,
            "balance": self.balance,
        }

    @classmethod
    def from_dict(cls, data):
        account = cls(data["name"], data["address"], data["phone"], data["email"], data["balance"])
        account.account_number = data["account_number"]  # Retain original account number
        return account

    def __str__(self):
        return f"\nName: {self.name}\nAccount type: {self.account_type}\nAccount number: {self.account_number}\nBalance: {self.balance}\n"


# For Savings and Mortgage accounts, override any specific behavior as needed
class SavingAccount(CurrentAccount):
    def __init__(self, name, address, phone, email, balance=0, interest_rate=2):
        super().__init__(name, address, phone, email, balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Apply interest to balance
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        self.balance = round(self.balance, 2)  # Round after adding interest
        print(f"Interest applied. New balance: {self.balance}")
        print("--------------------------------------------------")

    def to_dict(self):
        data = super().to_dict()
        data["interest_rate"] = self.interest_rate
        return data

    @classmethod
    def from_dict(cls, data):
        account = super().from_dict(data)
        account.interest_rate = data.get("interest_rate", 2)
        return account


class MortgageAccount(CurrentAccount):
    def __init__(self, name, address, phone, email, balance=0, interest_rate=5, monthly_repayment=0):
        super().__init__(name, address, phone, email, balance)
        self.account_type = "Mortgage"
        self.interest_rate = interest_rate
        self.monthly_repayment = monthly_repayment

    def apply_interest(self):
        # Apply interest to mortgage balance
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        self.balance = round(self.balance, 2)  # Round after adding interest
        print(f"Interest applied to mortgage. New balance: {self.balance}")

    def to_dict(self):
        data = super().to_dict()
        data["interest_rate"] = self.interest_rate
        data["monthly_repayment"] = self.monthly_repayment
        return data

    @classmethod
    def from_dict(cls, data):
        account = super().from_dict(data)
        account.interest_rate = data.get("interest_rate", 5)
        account.monthly_repayment = data.get("monthly_repayment", 0)
        return account

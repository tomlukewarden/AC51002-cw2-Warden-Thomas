class CustomerDetails:
    last_account_number = 1001  # Initial value; starts numbering from 1001

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


class CurrentAccount(CustomerDetails):
    def __init__(self, name, address, phone, email, balance=0):
        super().__init__(name, address, phone, email)
        self.account_number = CustomerDetails.last_account_number
        CustomerDetails.last_account_number += 1  
        self.account_type = "Current"
        self.balance = balance

    def __str__(self):
        return f"\nName: {self.name}\nAccount type: {self.account_type}\nAccount number: {self.account_number}\nBalance: {self.balance}\n"


class SavingAccount(CurrentAccount):
    def __init__(self, name, address, phone, email, balance=0, interest_rate=0.02):
        super().__init__(name, address, phone, email, balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate


class MortgageAccount(CurrentAccount):
    def __init__(self, name, address, phone, email, balance=0, interest_rate=0.05, monthly_repayment=0):
        super().__init__(name, address, phone, email, balance)
        self.account_type = "Mortgage"
        self.interest_rate = interest_rate
        self.monthly_repayment = monthly_repayment
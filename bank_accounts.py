class CustomerDetails:
    last_account_number = 1000  # Initial value; start numbering from 1001

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
        return f"Name: {self.name}\nAccount type: {self.account_type}\nAccount number: {self.account_number}\nBalance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def check_balance(self):
        print ("Balance of a/c {:d} is {:s}{:.2f}".format(self.account_number, self.currency, self.balance))

class SavingAccount(CurrentAccount):
    def __init__(self, name, account_number, address, phone, email, account_type, balance, statement, interest_rate):
        super().__init__(name, account_number, address, phone, email, account_type, balance, statement)
        self.interest_rate = interest_rate
        

class MortgageAccount(CurrentAccount):
    def __init__(self, name, account_number, address, phone, email, account_type, balance, statement, interest_rate, monthly_repayment, linked_account_number):
        super().__init__(name, account_number, address, phone, email, account_type, balance, statement)
        self.interest_rate = interest_rate
        self.monthly_repayment = monthly_repayment
        self.linked_account_number = linked_account_number

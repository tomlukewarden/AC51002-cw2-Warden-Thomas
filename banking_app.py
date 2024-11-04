class CustomerDetails:
    def __init__(self, name, account_number, address, phone, email):
        self.name = name
        self.account_number = account_number
        self.address = address
        self.phone = phone
        self.email = email
    

class CurrentAccount(CustomerDetails):
    def __init__(self, name, account_number, address, phone, email, account_type, balance, statement):
        super().__init__(name, account_number, address, phone, email)
        self.account_type = account_type
        self.balance = balance
        self.statement = statement
        

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

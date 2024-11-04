class CustomerDetails:
    def __init__(self, name, account_number, account_type, address, phone, email, balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.address = address
        self.phone = phone
        self.email = email
        self.balance = balance
        

class CurrentAccount:
    def __init__(self, account_number, account_type, balance, statement):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.statement = statement
        

class SavingAccount(CurrentAccount):
    def __init__(self, account_number, account_type, balance, statement, interest_rate):
        super().__init__(account_number, account_type, balance, statement)
        self.interest_rate = interest_rate
        

class MortgageAccount:
    def __init__(self, account_number, account_type, balance, statement, interest_rate, monthly_repayment, linked_account):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.statement = statement
        self.interest_rate = interest_rate
        self.monthly_repayment = monthly_repayment
        self.linked_account = linked_account

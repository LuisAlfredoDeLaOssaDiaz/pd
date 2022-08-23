import internal

class Bankaccount(internal.Internal):
    account:str
    bankname: str
    bankid: str

    def __init__(self, account, bankname, bankid):
        self.account = account
        self.bankname = bankname
        self.bankid = bankid
    def deposit(self, amount):
        self.amount = amount
    
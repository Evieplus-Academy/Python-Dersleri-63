class BankAccount:
    accounts = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.accounts.append(self)

    @classmethod
    def list_accounts(cls):
        for account in cls.accounts:
            print("Müşteri İsmi", account.name, "Hesap Bakiyesi", account.balance)


BankAccount("Ahmet", 10000)
BankAccount("Ayşe", 12000)
BankAccount.list_accounts()

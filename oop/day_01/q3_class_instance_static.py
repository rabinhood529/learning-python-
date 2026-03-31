class Bank_Account():
    bank_name = "Nepal Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Rs {amount} depsited to your account ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Rs {amount} deducted from your account ")
            print(f"New balance: Rs {self.balance}")
                
    @classmethod
    def get_bank_name(cls):
        print(cls.bank_name)

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        else: 
            return False
        

Bank_Account.get_bank_name()
print(Bank_Account.is_valid_amount(50))
acc = Bank_Account("Hari", 5000)
acc.deposit(1000)
acc.withdraw(10)
acc.withdraw(99)
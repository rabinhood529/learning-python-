class Account():
    
    def __init__(self, bal, account_no):
        self.bal = bal
        self.account_no = account_no
        


    def debit(self, amount):
        self.bal -= amount
        print(f"Rs.{amount} has been debited")


    def credit(self, amount):
        self.bal += amount
        print(f"Rs.{amount} has been credited")
        
    def balance(self, amount):
        return self.balance


s1 = Account(45000, 101234012)
print(s1.credit(500))

        
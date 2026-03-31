class Bank_Account():

    def __init__(self,owner, balance):
        self.__owner = owner
        self.__balance = balance


    def get_owner(self):
        return self.__owner
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Deposiut!")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("INvalid withdrawal!")

    def account_info(self):
        if self.__balance > 0:
            status = "Active"
        else:
            status = "Inactive"
            
        print(f"Owner: {self.__owner} | Balance: {self.__balance} | Status: {status}")

acc = Bank_Account("Ram", 5000)
acc.deposit(1000)
acc.withdraw(200)
acc.withdraw(9999)
acc.deposit(-50)
acc.account_info()
class Account:
    # constructor
    def __init__(self,customerId,customerName,balance):
        self.__customerId = customerId
        self.__customerName = customerName
        self.__balance = balance

    def deposit(self, amount):
        self.__balance=self.__balance + amount
        print(f"Rs.{amount} has been deposited in your account ")

    def widthdraw(self, amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            print(f"Rs.{amount} deducted from your account")
        else:
            print("Insufficient balance")

    def checkBalance(self):
        print(f"Your current balance is : {self.__balance}")

# object creation
obj = Account("ct101","user1",5000)
obj.checkBalance()
obj.deposit(1000)
obj.checkBalance()
obj.widthdraw(500)
obj.checkBalance()
# print(obj.__balance)
# print("hello user")
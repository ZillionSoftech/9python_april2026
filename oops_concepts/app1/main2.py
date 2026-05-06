import datetime
import json
import random

class Account:
    def __init__(self, customerId, customerName, balance, pin):
        self.__customerId = customerId
        self.__customerName = customerName
        self.__balance = balance
        self.__pin = pin
        self.__transactions = []
        self.__accountType = "Savings"
        self.__dailyLimit = 20000
        self.__lastWithdrawDate = None
        self.__dailyWithdrawAmount = 0

    # ---------------- SECURITY ----------------
    def verify_pin(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("PIN updated successfully")
        else:
            print("Invalid old PIN")

    # ---------------- BASIC OPERATIONS ----------------
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.__balance += amount
        self.__add_transaction("DEPOSIT", amount)
        print(f"Rs.{amount} deposited successfully")

    def withdraw(self, amount):
        today = datetime.date.today()

        if self.__lastWithdrawDate != today:
            self.__dailyWithdrawAmount = 0
            self.__lastWithdrawDate = today

        if amount > self.__dailyLimit:
            print("Exceeds single transaction limit")
            return

        if (self.__dailyWithdrawAmount + amount) > self.__dailyLimit:
            print("Daily withdrawal limit exceeded")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            self.__dailyWithdrawAmount += amount
            self.__add_transaction("WITHDRAW", amount)
            print(f"Rs.{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current Balance: Rs.{self.__balance}")

    # ---------------- TRANSACTION ----------------
    def __add_transaction(self, txn_type, amount):
        txn = {
            "type": txn_type,
            "amount": amount,
            "date": str(datetime.datetime.now())
        }
        self.__transactions.append(txn)

    def show_transactions(self):
        print("\nTransaction History:")
        for txn in self.__transactions:
            print(txn)

    # ---------------- TRANSFER ----------------
    def transfer(self, target_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            target_account.__balance += amount

            self.__add_transaction("TRANSFER_OUT", amount)
            target_account.__add_transaction("TRANSFER_IN", amount)

            print(f"Transferred Rs.{amount} to {target_account.__customerName}")
        else:
            print("Insufficient balance")

    # ---------------- INTEREST ----------------
    def apply_interest(self, rate=5):
        interest = (self.__balance * rate) / 100
        self.__balance += interest
        self.__add_transaction("INTEREST", interest)
        print(f"Interest of Rs.{interest} applied")

    # ---------------- ACCOUNT INFO ----------------
    def account_info(self):
        print("\n--- Account Details ---")
        print("ID:", self.__customerId)
        print("Name:", self.__customerName)
        print("Type:", self.__accountType)
        print("Balance:", self.__balance)

    # ---------------- FILE STORAGE ----------------
    def save_to_file(self):
        data = {
            "id": self.__customerId,
            "name": self.__customerName,
            "balance": self.__balance,
            "transactions": self.__transactions
        }

        with open(f"{self.__customerId}.json", "w") as f:
            json.dump(data, f)

        print("Account saved to file")

    def load_from_file(self):
        try:
            with open(f"{self.__customerId}.json", "r") as f:
                data = json.load(f)
                self.__balance = data["balance"]
                self.__transactions = data["transactions"]

            print("Account loaded successfully")
        except:
            print("No previous data found")

    # ---------------- UTILITIES ----------------
    def generate_statement(self):
        print("\n--- ACCOUNT STATEMENT ---")
        for txn in self.__transactions:
            print(f"{txn['date']} - {txn['type']} - Rs.{txn['amount']}")

    def set_account_type(self, acc_type):
        self.__accountType = acc_type

    def get_customer_name(self):
        return self.__customerName


# ---------------- BANK SYSTEM ----------------
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        cid = input("Enter Customer ID: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))
        pin = input("Set PIN: ")

        acc = Account(cid, name, balance, pin)
        self.accounts[cid] = acc

        print("Account created successfully")

    def login(self):
        cid = input("Enter Customer ID: ")
        pin = input("Enter PIN: ")

        acc = self.accounts.get(cid)

        if acc and acc.verify_pin(pin):
            print("Login successful")
            self.menu(acc)
        else:
            print("Invalid credentials")

    def menu(self, acc):
        while True:
            print("\n1.Deposit 2.Withdraw 3.Balance 4.Transfer")
            print("5.Transactions 6.Interest 7.Statement")
            print("8.Save 9.Load 10.Change PIN 0.Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                amt = float(input("Amount: "))
                acc.deposit(amt)

            elif choice == "2":
                amt = float(input("Amount: "))
                acc.withdraw(amt)

            elif choice == "3":
                acc.check_balance()

            elif choice == "4":
                target_id = input("Target ID: ")
                amt = float(input("Amount: "))
                target = self.accounts.get(target_id)
                if target:
                    acc.transfer(target, amt)
                else:
                    print("Target account not found")

            elif choice == "5":
                acc.show_transactions()

            elif choice == "6":
                acc.apply_interest()

            elif choice == "7":
                acc.generate_statement()

            elif choice == "8":
                acc.save_to_file()

            elif choice == "9":
                acc.load_from_file()

            elif choice == "10":
                old = input("Old PIN: ")
                new = input("New PIN: ")
                acc.change_pin(old, new)

            elif choice == "0":
                break

            else:
                print("Invalid choice")


# ---------------- MAIN ----------------
bank = BankSystem()

while True:
    print("\n--- BANK SYSTEM ---")
    print("1.Create Account")
    print("2.Login")
    print("0.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        bank.create_account()

    elif ch == "2":
        bank.login()

    elif ch == "0":
        break

    else:
        print("Invalid choice")
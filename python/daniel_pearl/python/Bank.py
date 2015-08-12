#Banks
""" An account file for out simple bank."""

class Account:
    """Account class that stores account info"""
    def __init__(self, balance, customer, account_type="checking"):
        self.balance = balance
        self.type = account_type
        self.owner = customer

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds to withdraw.")
        else:
            self.balance -= money

    def balance(self):
        return self.balance

    def check_balance(self):
        print('Your balance is ${:,.2f}'.format(self.balance))

    def interest(self, percentage):
        self.balance += (1+(percentage/100))

class Customer:
    """A class that tracks customer in bank"""
    def __init__(self, first_name, last_name, email):
        self.accounts = {}
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def deposit(self,money,account_name):
        new_amount = self.accounts[account_name].deposit(money)
        print("${0:,.2f} was successfully deposited to {1}".format(money, account_name))

    def withdraw(self, money, account_name):
        new_amount = self.accounts[account_name].withdraw(money)
        print("${0:,.2f} was successfully withdrawn from {1}".format(money, account_name))

    def open_account(self, initial_balance, name, acount_type = "checking"):
        new_account = Account(self, initial_balance, account_type="checking")
        self.accounts[name]=new_account

    def close_account(self, name):
        del self.accounts[name]

    def show_account(self):
        print(self.first_name + " " + self.last_name)
        print(self.email)

"""
"""
class Bank:
    def __init__(self):
        self.customers = {}
        self.savings_interest = 1.07

    def new_customer(self, first_name, last_name, email):
        new_customer = Customer(first_name, last_name, email)
        self.customers[email] = new_customer

    def remove_customer(self, email):
        del self.customers[email]

    def show_customer_info(self, email):
        self.customers[email].email
        print("Hello {} {}, and welcome to the bank".format(customers.first_name, customers.last_name))
        return self.customers[email]
        self.customer.show_accounts()

    def customer_deposit(self, email, money, account_name):
        self.customers[email].deposit(money,account_name)

    def customer_withdraw(self, email, money, account_name):
        self.customers[email].withdraw(money,account_name)

    def make_customer_account(self, email, money, account_name, account_type="checking"):
        self.customers[email].open_account(money, account_name, account_type)


    def remove_customer_account(self, email, account_name):
        self.customers[email].close_account(account_name)

#
# new_customer = Customer("Daniel","Pearl", "danielaaronpearl@gmail.com")
# new_customer.show_account()
#
# new_account = Account(100,"Daniel")
# new_account.check_balance()

new_bank = Bank()
#new_bank.make_customer_account("danielaaronpearl@gmail", 60, "Daniel")
new_bank.new_customer("Daniel", "Pearl", "danielaaronpearl@gmail.com")
print(new_bank.show_customer_info("danielaaronpearl@gmail.com"))

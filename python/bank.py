# An account file for our Si.MPLE Bank
# refer to Slack for UML diagram
# >>>--------------------------------->


class Account:
  """
  Account class that stores account info.
  """
  def __init__(self, balance, account_type = "checking"):
    self.balance = balance
    self.account_type = account_type.capitalize()

    print("\n{} account established. Current balance is: {}".format(self.account_type, self.print_balance()))

  def deposit(self, money):
    self.balance += money
    print("Deposit complete. Your {} balance is: {}".format(self.account_type, self.print_balance()))

  def withdraw(self, money):
    if money > self.balance:
      print("Insufficient funds, Your {} balance is: {}".format(self.account_type, self.print_balance()))
    else:
      self.balance -= money
      print("Withdraw complete. Your {} balance is: {}".format(self.account_type, self.print_balance()))

  def print_balance(self):
    return '\n${:,.2f}\n'.format(self.balance)

  def interest(self, percentage):
    self.balance += self.balance  * percentage / 100
    print("Interest earned of {}% on your {} account. Your {} balance is: {}".format(percentage, self.account_type, self.account_type, self.print_balance()))


class Person:
  """
  Person class that tracks Persons in our bank.
  """
  # initializes the Person class
  def __init__(self, first_name, last_name, email):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.accounts = {}

  def open_account(self, initial_balance, account_name, account_type="Checking"):
    new_account = Account(initial_balance, account_type)
    self.accounts[account_name.lower()] = new_account

  def close_account(self, account_name):
    self.show_accounts()
    if account_name.lower() not in self.accounts:
      print(">>> '{}' account type does not exist. Try again.\n".format(account_name))
    if account_name.lower() in self.accounts:
      confirmation = input("Type YES to confirm '{}' account closure. NO to cancel: ".format(account_name.title()))
      if confirmation.lower() == "yes":
        del self.accounts[account_name.lower()]
        print("'{}' account closed. Have a good day!\n".format(account_name.title()))
      else:
        print(">>> Transaction cancelled.")

  def show_accounts(self):
    """
    Display on the screen all of a Person's account info
    """
    if len(self.accounts) == 0:
      print(">>> No accounts established for {} {}\n".format(self.first_name, self.last_name))
    else:
      print("Account(s) for {} {}:".format(self.first_name, self.last_name))
      print("---------------")
      for k, v in self.accounts.items():
        print("{} >>> {}".format(k.title(), v.print_balance()))


class Bank:
  """
  Bank class handles the Accounts and Persons.
  """
  def __init__(self):
    self.customers = {}
    self.savings_interest = 1.07

  def new_customer(self, first_name, last_name, email):
    new_customer = Person(first_name, last_name, email)
    self.customers[email.lower()] = new_customer

  def remove_customer(self, email):
    del self.customers[email.lower()]

  def show_customer_info(self, email):
    self.customers[email].show_accounts()

  def make_customer_account(self, email, money, account_name, account_type="checking"):
    self.customers[email.lower()].open_account(money, account_name, account_type)

  def remove_customer_account(self, email, account_name):
    self.customers[email.lower()].close_account(account_name)

  def customer_deposit(self, email, money, account_name):
    self.customers[email.lower()].deposit(money, account_name)

  def customer_withdraw(self, email, money, account_name):
    self.customers[email.lower()].withdraw(money, account_name)




# TESTS
# >>>------------------------------------->
# myAccount = Account(1000, "Michael")
# myAccount.deposit(50)
# myAccount.withdraw(75)
# myAccount.withdraw(1000)
# myAccount.interest(20)
# myAccount.print_balance()

# me = Person("Michael", "Williams", "me@gmail.com")
# me.open_account(1000, "Car Fund", "savings")
# me.open_account(2000, "House Fund", "savings")
# me.show_accounts()
# me.close_account("Checking")
# me.show_accounts()
# me.close_account("Car fund")
# me.show_accounts()

myBank = Bank() # make a bank
mw = myBank.new_customer("Michael", "Williams", "mw@email.com")
myBank.show_customer_info("mw@email.com")
myBank.make_customer_account("mw@email.com", 1000, "Car Fund")
myBank.customer_deposit("mw@email.com", 1000, "Car Fund")









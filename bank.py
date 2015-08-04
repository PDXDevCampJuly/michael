# An account file for our Si.MPLE Bank
# refer to Slack for UML diagram
# >>>--------------------------------->


class Account:
  """
  Account class that stores account info
  """

  def __init__(self, balance, person, account_type = "checking"):
    self.balance = balance
    self.owner = person
    self.account_type = account_type

  def deposit(self, money):
    self.balance += money
    print("Deposit complete. Your current balance is: {}".format(self.print_balance()))

  def withdraw(self, money):
    if money > self.balance:
      print("Insufficient funds, your balance is: {}".format(self.print_balance()))
    else:
      self.balance -= money
      print("Withdraw complete. Your current balance is {}".format(self.print_balance()))

  def print_balance(self):
    print('${:,.2f}'.format(self.balance))

  def interest(self, percentage):
    self.balance += self.balance  * percentage / 100


class Person:
  """
  Person class that stores person info
  """

  def __init__(self, first_name, last_name, email):
    self.first = first_name
    self.last = last_name
    self.email = email

  def open_account(initial_balance, type):
    pass

  def close_account(account_type):
    pass



myAccount = Account(1000, "Michael")
myAccount.deposit(50)
myAccount.withdraw(75)
myAccount.withdraw(1000)
myAccount.print_balance()










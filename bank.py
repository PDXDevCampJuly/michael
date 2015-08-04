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

    print("\nWelcome {}. {} account established. Current balance is: {}".format(self.account_type, self.print_balance()))

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

  def __init__(self, first_name, last_name, email):
    self.first = first_name
    self.last = last_name
    self.email = email
    self.accounts = {}

  def open_account(self, initial_balance, account_name, account_type="Checking"):
    new_account = Account(initial_balance, account_name, account_type)
    self.accounts[account_type] = new_account

  def close_account(self, account_type):
    self.show_accounts()
    if account_type not in self.accounts:
      print("{} account type does not exist. Try again.".format(account_type))
    if account_type in self.accounts:
      confirmation = input("Type YES to confirm {} account closure. NO to cancel: ".format(account_type.capitalize()))
      if confirmation.lower() == "yes":
        del self.accounts[account_type]
        print(">>> {} account closed. Have a good day!".format(account_type.capitalize()))
      else:
        print(">>> Transaction cancelled.")


  def show_accounts(self):
    """
    Display on the screen all of a Person's account info
    """

    if len(self.accounts) == 0:
      print("No accounts established for {} {}:".format(self.first, self.last))
    else:
      for k, v in self.accounts.items():
        print("Here are the account(s) for {} {}".format(self.first, self.last))
        print("----------------------------------")
        print("{} >>> {}".format(k.capitalize(), v.print_balance()))


class Bank:

  def __init__(self):
    self.customers = {}
    self.savings_interst = 1.07

  def new_customer(self, first_name, last_name, email):
    new_customer = Person(first_name, last_name, email)
    customers[email] = new_customer
    pass

  def remove_customer(self, email):
    pass

  def show_customer_info(self, email):
    pass

  def customer_deposit(self, email, money, account_name):
    pass

  def customer_withdraw(self, email, money, account_name):
    pass

  def make_customer_account(self, email, money, account_name):
    pass

  def remove_customer_account(self, email, account_name):
    pass


# myAccount = Account(1000, "Michael")
# myAccount.deposit(50)
# myAccount.withdraw(75)
# myAccount.withdraw(1000)
# myAccount.interest(20)
# myAccount.print_balance()

me = Person("Michael", "Williams", "me@gmail.com")
me.open_account(1000, "Car Fund", "savings")
# me.show_accounts()
# me.close_account("Checking")
# me.show_accounts()
# me.close_account("savings")
# me.show_accounts()









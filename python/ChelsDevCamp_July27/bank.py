""""""
class Account:
	def __init__(self, balance, account_type="checking"):
		self.balance = balance
		self.account_type = account_type 

	def deposit(self, money):
		self.balance += money

		return self.balance

	def withdraw(self, money):
#Withdraw takes money out from the balance

		if money > self.balance:
			print("You don't have enough money in your account. Your current balance is", 
				print_balance(self))
		else:
			self.balance -= money

		return self.balance



	def check_balance(self):
		return self.balance

	def print_balance(self):
		return'${:,.2f}'.format(self.balance)


	def intrest(self, percentage):

		self.balance += percentage



#	def test_account(self):

# test = account(500, "Chelsea")
# print(test.print_balance())
# test.deposit(5)
# print(test.print_balance())
# test.withdraw(5)
# print(test.print_balance())
# test.withdraw(700)
# print(test.print_balance())
# test.intrest(2.50)
# print(test.print_balance())

class Person:
	def __init__(self, first_name, last_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.accounts = {}

		

	def openaccount(self, inital_balance, account_name, account_type="checking"):
		new_account = Account(inital_balance, account_type)
		self.accounts[account_name] = new_account

#er

	def deposit(self, money, account_name):
 		new_amount = self.accounts[account_name].deposit(money)
 #		print("${0:,.2f}" was )

	def withdraw(self, money, account_name):
		new_amount = self.accounts[account_name].withdraw(money)

#I want it to take the info they give and see if it's in the string. 
#if it is tell them and if it's not
#put info into string
#Put the email, first name and last into a 

	def closeaccount(self, account_name):
		del self.accounts[account_name]


	def show_accounts(self):
		for  k,v in self.accounts.items():
			print("There is ", v.print_balance(), "in the account", k)


# test = Person("Chelsea", "Dover", "email@mail.com")
# print(test.show_accounts())
# test.openaccount(500, "Chelsea")
# print(test.show_accounts())
# #test.openaccount(20, "other account")
# #print(test.show_accounts())
# test.closeaccount("Chelsea")
# print(test.show_accounts())
# test.openaccount(700, "savings")
# print(test.show_accounts())
####
#####
######
#######
########
#########
########
######
####
###
##
#
##
###
####
####
		

class Bank:
	def __init__(self):
		self.customers = {}
		self.savings_intrest = 1.07

	def new_customer(self, email):
		new_customer = Person(first_name, last_name, email)
		self.customers[email] = new_customer

	def remove_customer(self, email):
#		closeaccount()
#I want this one to delete all info about the custumer. 
		del self.customer[email]

#		pass

	def show_customer_infro(self, email):
		customer_info = self.customers[email]
		customer.show_accounts()
		#print("Hello {} {} and welcom ")


	def customer_deposit(self, email, money, account_name):
	#	self.customer[email] 
	#	new_amount = 
		self.customers[email].deposit(money, account_name)
#I want this to take an email and find what account they want to deposit into
#Deposit into the right account

	def costumer_withdraw(self, email, money, account_name):
		 #new_amount = 
		 self.customers[email].withdraw(money, account_name)

	def make_costumer_account(self, email, money, account_name, account_type = "Checking"):
#		new_amount = 
		self.customers[email].openaccount(money, account_type)
#		self.accounts[account_name] = account_name

	def remove_costumer_account(self, email, account_name):
#		del self.accounts[email]
		self.customers[email].closeaccount(money, account_type)


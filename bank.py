
class BankAccount():
	def __init__(self, account_number, balance, date_of_opening, account_name):
		self.account_number=account_number
		self.balance=balance
		self.date_of_opening=date_of_opening
		self.account_name=account_name

	def deposit(self):
		return self.deposit

	def withdraw(self,amt_to_be_withdrawn):
		if amt_to_be_withdrawn>self.balance:
			return "Insufficient balance"
		else:
			return ("Amount withdrawn: ",self.amt_to_be_withdrawn)

	def check_balance(self):
		print("Current balance is: ",self.balance)

	def customer_details(self):
		print("Customer's Account number: ", self.account_number)
		print("Customer's Balance: ", self.balance)
		print("Customer's Date of opening:", self.date_of_opening)
		print("Customer's Account name:", self.account_name)

bank= Customer(128, 62000, 12/09/2021, "EQ27")
customer.customer_details()
class User:
	__name = ''
	__email = ''

	def __init__(self, name, email):
		self.__name  = name
		self.__email = email

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_email(self, email):
		self.__email = email

	def get_email(self):
		return self.__email

	def info(self):
		return 'Users name is {} and email is {}.'.format(self.__name, self.__email)

'''
maksym = User('Maksym', 'maksym@mail.com')

print(maksym.get_email())
print(maksym.info())

os = open('test.txt', 'a+')
os.write('\nUser name: ' + maksym.get_name())
os.write('\nUser email: ' + maksym.get_email())
os.close()
'''

class Customer(User):
	def __init__(self, name, email, balance):
		self.__name = name
		self.__email = email
		self.__balance = balance
		super(Customer, self).__init__(name, email)

	def set_balance(self, balance):
		self.__balance = balance

	def get_balance(self):
		return self.__balance

	def about(self):
		return '{} has a balance of {}$ and can be contacted at {}.'.format(self.__name, self.__balance, self.__email)


maksym = Customer('Maksym', 'max@gmail.com', 5400)
maksym.set_name('Max')
maksym.set_email('maksym@mail.com')
maksym.set_balance(2600)


#print(maksym.about())

class Worker():
	pass

bob = Worker()
bob.name = 'Tim'

#print(bob.name)

class Employee():

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay
		self.email = fname + '.' + lname + '@company.com'

		Employee.num_of_emps += 1 


	def fullname(self):
		return '{} {}'.format(self.fname, self.lname) 

	def apply_raise(self):
		#self.pay = int(self.pay * Employee.raise_amount)
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		#pass	
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		fname, lname, pay = emp_str.split('-')
		return cls(fname, lname, pay)

	#first argument not 'self' and not 'cls'
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	


dan = Employee('Dan', 'Conelly', 50000)
tim = Employee('Tim', 'Filen', 70000)

#print(dan.email)
#print(dan.fullname())
#print(Employee.fullname(dan))
'''
print(dan.pay)
Employee.apply_raise(dan)
print(dan.pay)
'''

#print(Employee.raise_amount)
'''
print(Employee.__dict__)
print('***************************')
print(dan.__dict__)
'''

#Employee.raise_amount = 1.07
#dan.raise_amount = 1.02
'''
Employee.set_raise_amt(1.09)

print(Employee.raise_amount)
print(dan.raise_amount)
print(dan.raise_amount)
'''

#print(dan.__dict__)
#print(Employee.num_of_emps)


emp_str_1 = 'Will-Smith-70000'
emp_str_2 = 'Kim-Johnsson-50000'
emp_str_1 = 'Brad-Karlsson-40000'

#print(emp_str_1.split('-'))
fname, lname, pay = emp_str_1.split('-')

emp_1 = Employee(fname, lname, pay)

new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.__dict__)

import datetime
my_date = datetime.date(2018, 4, 6)
#print(my_date)
#print(Employee.is_workday(my_date))
my_date1 = '2018-08-08'
#print(my_date1.weekday())

#repr(dan)


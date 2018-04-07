class Employee():

	raise_amount = 1.04

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.email = fname + '.' + lname + '@company.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname) 

	def apply_raise(self):
		#self.pay = int(self.pay * Employee.raise_amount)
		self.pay = int(self.pay * self.raise_amount)

					# OVERLOAD OPERATORS 
	# for debug and loging
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)

	# more readable representation	
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	#add 2 employees and get sum of pay as result
	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname()) - 1


class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, fname, lname, pay, prog_lang):
		super().__init__(fname, lname, pay)
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self, fname, lname, pay, employees = None):
		super().__init__(fname, lname, pay)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())


#print(help(Developer))

dev_1 = Developer('Dan', 'Conelly', 50000, 'Python')
dev_2 = Developer('Tim', 'Filen', 70000, 'Java')

mgr_1 = Manager('Joe', 'Smith', 90000, [dev_1])

#print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

#print(mgr_1.print_emps())



'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)
'''
#print(isinstance(mgr_1, Manager))
#print(issubclass(Manager, Employee))
dev_3 = Employee('Dan', 'Conelly', 50000)
dev_4 = Employee('Kim', 'Flinstone', 70000)


# OVERLOAD OPERATORS
'''
print(repr(dev_3))
print(str(dev_3))

print(dev_3.__repr__())
print(dev_3.__str__())
'''

#print(int.__add__(1, 2))
#print(str.__add__('a', 'b'))



print(dev_3 + dev_4)
print(len('test'))
print('test'.__len__())

print(len(dev_3))


print(dev_3.__dir__())
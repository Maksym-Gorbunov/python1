'''
# open and write text to the file
fo = open('test.txt', 'w+')
text = 'Maksym write this code again'
fo.write(text)
fo.close()

# open and append text in new line
fo = open('test.txt', 'a')
text = '\nand this one ...'
fo.write(text)
fo.close()

# read from the file
fo = open('test.txt', 'r+')
text = fo.read()

#check if file is empty
import os
a = os.stat('test.txt').st_size
print('File size is: ', a)

if a == 0:
	print('File is empty!')
else:
	print(text)
fo.close()

# read by line
fo = open('test.txt')
lines = fo.readlines()
'''

'''
import maxFunctions
maxFunctions.hello('Maksym')
'''

'''
from maxFunctions import hello
hello('Olga')
'''
users = ['Dan', 'John', 'Billy', 'Peter', 'Tim']

'''
for i in range(0, len(users)):
	print(users[i])
'''
'''
i = 0
while i != len(users):
	print(users[i])
	i += 1
''' 
'''
for item in users:
	print(item+'...')
'''

class Employee():

	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		#self.email = fname + '.' + lname + '@company.com'
	
	@property
	def email(self):
		return '{}.{}@hotmail.com'.format(self.fname, self.lname)

	@property
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname) 

	@fullname.setter
	def fullname(self, name):
		fname, lname = name.split(' ')
		self.fname = fname
		self.lname = lname

	@fullname.deleter
	def fullname(self):
		self.fname = None
		self.lname = None
		print('Fullname was deleted!')



emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Bil Json'

print(emp_1.fname)
print(emp_1.lname)
print(emp_1.fullname)
print(emp_1.email)

print(emp_1.fullname.split())

del emp_1.fullname
print(emp_1.fullname)
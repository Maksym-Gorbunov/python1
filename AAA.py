path_to = os.environ.get('USERPROFILE')
file_path = os.path.join(path_to, 'test.py')	# make path easy and right

# OVERLOAD OPERATORS
__repr__
__str__
print(int.__add__(1, 2))		# 3		add if int
print(str.__add__('a', 'b'))	# ab	concatenate if str


# .append
# .remove

.format
super().__init__(fname, lname, pay)

return NotImplemented

.split(' ')

f'{a} and {b}'	#f-string

.__dir__()	
dir(a)	# see all methods
help(a)
help(a.lower)

#int
round(3.73)	# 4
round(3.76, 1)	# 3.8
abs(-3)		# 3

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# assignment	    a = 42

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# enumerate	# return index and value in for loop ex.

'''
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
-art_courses = {'History', 'Math', 'Scine', 'Geography'}
-
-print(cs_courses)
-print(cs_courses.intersection(cs_courses))
-print(cs_courses.difference(cs_courses))
-print(cs_courses.union(cs_courses))	# all together

{'History', 'Math'}
'''

# print(student.keys())
# print(student.values())
# print(student.items())

# id(a)	#return adress memory
# CONDITIONALS
'''
x = 7

# Basic If
if x < 6:
    print('This is true')
  
# If Else
if x < 6:
    print('This is true')
else:
    print('This is false')
    
# Elif
color = 'red'

if color == 'red':
    print('Color is red')
elif color == 'blue':
    print('Color is blue')
else:
    print('Color is not red or blue')
    
# Nested if
if color == 'red':
    if x < 10:
        print('Color is red and x is less than 10')
        
# Logical operators
if color == 'red' and x < 10:
    print('Color is red and x is less than 10')
'''


# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
'''
condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

'''
'''
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print(f'Welcome {user}')
'''
# is: check if values in the same memory, same if int or str... and different if list... 

a = [1,2,3]
b = [1,2,3]
c = 'hello'
d = 'hello'
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(a))
# print(id(c))
# print(id(d))
# print(c==d)
# print(c is d)
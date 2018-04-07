student = {'name': 'Maksym', 
		   'age': 32, 
		   'email': 'maksym@mail.com', 
		   'pr_lang': ['PHP', 'Python', 'JS']}

# print(student['pr_lang'][1])	

# print(student['name'])
# print(student['pay'])		#return error if not exist
# print(student.get('name'))
# print(student.get('pay'))	#return None if not exist
# print(student.get('pay', 'Not Found'))	#return 'Not Found' if not exist

# student['salery'] = 25000
# student['name'] = 'Tim'

# student.update({'name': 'Bobby', 'salery': 27000})
# del student['name']
# name = student.pop('name')

# print(name)
'''
for index, item in enumerate(student):
	print(index, item)
'''
# print(len(student))

# print(student.keys())
# print(student.values())
# print(student.items())

for key, value in student.items():
	print('{}: {}'.format(key, value))
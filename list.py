lang = ['C++', 'Java', 'PHP']

lang2 = ['CSS', 'JavaScript']

lang.index('PHP')

#min
#max
#sum

# lang.reverce()
# lang.sort()
# lang.sort(reverce=True)

# sorted(lang)	# return sorted list not changing original

#lang.pop()	# remove last element
#print(lang.pop())	# return popped element

#lang.remove('PHP')	 

#lang.extend(lang2)	# append all values to the end	

#lang.append('CSS')	# add to the end

#lang.insert(0, 'HTML')	insert to index + value
'''
b = [6,1,3,5,9,2]
print(lang) 
print(b)
# c=b.sort()
c = sorted(b)
print(b)
print(c)
'''

#print('C++' in lang) # True

'''
for index, l in enumerate(lang, start=1):
	print(f'{index}: {l}')
'''

lang_str = ', '.join(lang)
lang_new = lang_str.split(', ')

'''
print(lang)
print(lang_str)
print(lang_new)
'''
#************************* Tuples - immutable  **************************************
-
-
-# Mutable
-list_1 = ['History', 'Math', 'Physics', 'CompSci']
-list_2 = list_1
-
-print(list_1)
-print(list_2)
-
-# list_1[0] = 'Art'
-
-# print(list_1)
-# print(list_2)
-
-
-# Immutable
-# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
-# tuple_2 = tuple_1
-
-# print(tuple_1)
-# print(tuple_2)
-
-# tuple_1[0] = 'Art'
-
-# print(tuple_1)
-# print(tuple_2)
-
-# Sets
-cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
-art_courses = {'History', 'Math', 'Scine', 'Geography'}
-
-print(cs_courses)
-print(cs_courses.intersection(cs_courses))
-
-
-# Empty Lists
-empty_list = []
-empty_list = list()
-
-# Empty Tuples
-empty_tuple = ()
-empty_tuple = tuple()
-
-# Empty Sets
-empty_set = {} # This isn't right! It's a dict
-empty_set = set()
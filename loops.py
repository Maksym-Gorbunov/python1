# LOOPS

#FOR LOOP
people = ['John', 'Sara', 'Tim', 'Bob']
'''
for person in people:
    print('Current Person: ', person)
    
# Iterate by seq index
for i in range(len(people)):
    print('Current Person: ',people[i])
    
for i in range(0, 10):
    print(i)
    
# WHILE lOOP

count = 0
while count <= 10:
    print('Count: ', count)
    if count == 5:
        break
    count = count + 1
 

while True:
    # if x == 5:
    #     break
    print(x)
    x += 1
'''

nums = [1,2,3,4,5]
'''
for num in nums:
	if num == 3:
		print('Found!')
		#break;				#	break the loop
		continue;			#	skip, and go to text loop
	print(num)
'''
'''
for num in nums:
	for letter in 'abc':
		print(num, letter)
'''
'''
for i in range(10):		#10 loops (0 to 9)
	print(i)
'''
'''
for i in range(1, 11):		#10 loops (1 to 10)
	print(i)
'''

x = 0

while x < 10:			# 0 to 9
	#if x == 6:
	#	break
		#continue
	print(x)
	x += 1

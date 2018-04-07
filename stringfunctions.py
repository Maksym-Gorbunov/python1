# STRING FUNCTIONS

myStr = 'Hello There World1'

# Capitalize
print(myStr.capitalize())

# Swap case
print(myStr.swapcase())

# Get length
print(len(myStr))

# Replace
print(myStr.replace('World', 'Everyone'))  #replace string and create new variabel, dont overwrite original

# Count
sub = "H"
print(myStr.count(sub))	#count total in string

# Startswith
print(myStr.startswith('Hello'))

# Endswith
print(myStr.endswith('!'))

# Split to list
print(myStr.split())

# find
print(myStr.find('H'))  # index start from

# index
print(myStr.index('H'))

#Is all alphanumeric
print(myStr.isalnum())

#Is all alphabetic
print(myStr.isalpha())

# Is all numeric
print(myStr.isnumeric())


print(message[:5])
print(message[3:])
print(message[0:5])
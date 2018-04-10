import os

os.chdir('C:/Python36')	                # change directory
print(os.getcwd())	                    # current working directory

# print(dir(os))	                    # all attributes and methods of os module

# os.mkdir('test1')				        # create dir
# os.makedirs('test2/subtest')	        # create dir and sub dirs

# os.rmdir('test1')				        # remove dir
# os.removedirs('test2/subtest')	    # remove dir and sub dirs

# os.rename('test.txt', 'test2.txt')	# rename file
# os.rename('test1', 'test')			# rename folder

# print(os.stat('test2.txt'))			# file info
# print(os.stat('test2.txt').st_size)	# file size

'''
timestamp = os.stat('test2.txt').st_atime	# file time in timestamp
from datetime import datetime 
print(datetime.fromtimestamp(timestamp0))	# readable time
'''

# print(os.listdir())		            # show all files and dirs

# loop through the tree
'''
for dirpath, dirnames, filenames in os.walk('C:/Python36'):
	print('Current Path', dirpath)
	print('Directories', dirnames)
	print('Files', filenames)
	print()
'''

print(os.environ.get('USERPROFILE'))				# get environments, home

#'test.txt'

# file_path = os.environ.get('USERPROFILE') + 'test.py'				# ease to miss '/' or '\'
path_to = os.environ.get('USERPROFILE')
file_path = os.path.join(path_to, 'test.py')	# make path easy and right
print(file_path)								# C:\Users\MAXXX


# create new dir if not exist
'''
my_directory = 'c:/python36/maxcoder'
import os
if not os.path.exists(my_directory):
    os.makedirs(my_directory)
'''


# print(os.path.basename('some_dir/some_file.txt'))		# some_file.txt
# print(os.path.dirname('some_dir/some_file.txt'))		# some_dir
# print(os.path.split('some_dir/some_file.txt'))		# ('some_dir', 'some_file.txt')

# print(os.path.exists('some_dir/some_file.txt'))		# if exist return True

# print(os.path.isdir('some_dir/some_file'))			# if dir return True
# print(os.path.isfile('some_dir/some_file.txt'))		# if file return True

# print(os.path.splitext('some_dir/some_file.txt'))		# ('some_dir/some_file', '.txt')

# print(dir(os.path))									# all attributes and methods of os module
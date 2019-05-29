import os
import glob
import datetime

'''
 This script deletes recent pictures that have been uploaded. 
 Make sure you change the absolute path so that it has your username in it.

'''

'''
 Possible enhancements would be to ask the user which extension types
 he wants to delete and the path where the script should look at. 
 
 Givng the possibility to pass arguments to give the user those options would
 be the way to go. 

'''

# absolute path of the directory where the script should be executed on
absolute_path = '/Users/insert_your_username_here/Downloads/'

os.chdir(absolute_path)

print('\n### Script ###\n')

print('We are at {}\n'.format(os.getcwd()))

print('This script will delete recently uploaded pictures in the downloads directory.\n')

print('Here is a list of recent uploads:\n')

# tuple of multiple filetypes
file_types = ('*.jpg', '*.JPG', '*.png')

files = []

# loading all images
for file_type in file_types:
	files.extend(glob.glob(absolute_path + file_type))

print(files,'\n')


# parsing user input
while True:
	response = input('Confirm deletion? Press y/n: ')

	if(response == 'y'):
		break
	elif(response == 'n'):
		print('Exiting now.')
		exit()
	else:
		print('Incorrect input. Please try again.')


for file in files:
	try:
		os.remove(file)
	except Exception as e:
		print(e)


print('Deletion confirmed.')

exit()


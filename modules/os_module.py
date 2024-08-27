import os

# get more info about all the functionality of a module
print(dir(os))
print(dir(os.path))

# print the current directory
print(os.getcwd())

# navigate to any location in your desktop
os.chdir('D:/Coding/Python/')

# get all the files/folders in a directory
print(os.listdir()) 

# making a new folder in the directory
os.mkdir('test') # use for singular directory creation
os.makedirs('test/test-example') # creates directory and subdirectory multiple folders

# delete folders
os.rmdir('test/test-example') # delete one folder
os.removedirs('test/test-example') # removes directory and subdirectory multiple folders

# rename a file and folder
os.rename('test', 'test2')

# # print all information about a certain file
print(os.stat('test.txt'))

# see complete directory tree
os.walk('filepath') #(dirpath, dirnames, filename)

# environment variables for PC
os.environ

# OS.PATH
# create a path for a destination
os.path.join()

# get the filename of a directory
print(os.path.basename(os.getcwd()))

# get the directory name of a path
print(os.path.dirname(os.getcwd()))

# get all paths in a path
print(os.path.split('/test/test2.txt'))

# find if a path exists
print(os.path.exists('python_basics'))

# check if a file exists
print(os.path.isfile('intro_1.py'))

# split the path and get the extension
print(os.path.splitext('path'))
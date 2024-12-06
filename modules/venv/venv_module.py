# Virtual Environments
# the purpose of a virtual environment is to have a space where we can install packages that are specific to a certain project
# python -m venv venv
# usually name it venv 

# Export the packages for a specific package -> requirements.txt file
'''
1. create a new requirements.txt file
2. do a pip freeze 
3. copy all the files from the pip freeze into the requirements.txt
'''


# Import the packages from a requirements.txt file
# create a virtual environment
'''
1. Find the path to the file
2. pip install -r requirements.txt
'''

# never put files/folders in the venv package
# dont commit the virtual environment to github (only add the requirements.txt)
# Create a file to rename files to make sure they are sorted in a directory
# This is useful when for example you download music and all the songs in an album are not sorted properly
import os

os.chdir('') # directory where the files are located

print(os.getcwd()) # print the directory

for f in os.listdir(): # get all individual files
    print(f) # print each file
    file_name, file_ext = os.path.splitext(f) # gives us a tuple with the file name and the extension at the end
    f_title, f_course, f_num = file_name.split('-') # seperate the information into different segments
    
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) # get rid of white space and the hashtag zfill pads the numbers with a zero in the front
    
    new_name = f'{f_num}-{f_title}-{file_ext}' # the format we want (number in the front)
    
    os.rename(f, new_name)
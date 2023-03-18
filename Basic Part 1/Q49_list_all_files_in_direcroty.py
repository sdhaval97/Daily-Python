# Q. To list all the files in the directory

# importing listdir, isfile and join 
from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('C:/Users') if isfile(join('C:/Users', f))]

print(files_list)

# the os module has some built-in functions that work with the files and folders in our computer
# listdir() function is used to make all the files and folders in a specified folder
# isfile() checks if the item is a file and not folder
# join is used to join the folder path and filename together
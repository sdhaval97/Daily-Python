# Q. To get the date and time of the file creation

# importing time and os.path
import time, os.path

#printing out the date and time
print("Last modified: ", time.ctime(os.path.getmtime("Boilerplate_with_bash.txt")))
print("Created: ", time.ctime(os.path.getctime("Boilerplate_with_bash.txt")))

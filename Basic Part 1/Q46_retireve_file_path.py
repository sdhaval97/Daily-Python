# Q. To retrieve the path and name of the file currently executing

# importing the os module
import os

#printing out the filename
print("Current file: ", os.path.realpath(__file__))


# os module helps us interact with the operating system of the machine we are working on
# __file__ variable is a built-in variable that contains the name of the file
# realpath() gives us the canonical path of the file
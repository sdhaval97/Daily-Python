# Q. To access environment variables

# importing os module
import os

# Accessing all environment variables
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['PATH'])
print('*----------------------------------*')

# os.environ gives us all the variables currently set in the system
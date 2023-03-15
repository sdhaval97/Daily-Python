# Q. To check the python shell version if it is 32 or 64 bit

# importing struct
import platform

# Checking if 32 or 64 bit
print(platform.architecture()[0])


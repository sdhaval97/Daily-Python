# Q. To check the python shell version if it is 32 or 64 bit

# importing struct
import platform

# Checking if 32 or 64 bit
print(platform.architecture()[0])

# the platform module gives an interface to access the information about the underlying
# platform python is running on
# architecture function of the platform module returns a tuple containing the information
# about the architecture of the underlying python platform
# the 0th index of the tuple contains the bits of the architecture
# the 1st index contains the build of the python interpreter. 
# in this case it returns Windows PE means it was built for windows platform that is 
# portable and executable (PE)


# Q. To call an external command

# importing call from subprocess
import psutil

# calling ls -l command 
print(psutil.cpu_count())

# the psutil module is a third-party python module that provides an interface to retrieve info
# about the system processes and system utilization
# the cpu_count gives us the number of logical cpus and processors in the system
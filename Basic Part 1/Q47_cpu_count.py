# Q. Printing th number of CPUs used

# importing multiprocessing
import multiprocessing

# printing out the number of cpus
print(multiprocessing.cpu_count())

# the multiprocessing module allows a program to run multiple cpus
# to perform tasks simultaneously
# cpu_count returns the number of cpus used
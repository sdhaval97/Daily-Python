# Q. To get the execution time

# importing time
import time

# Defining the function
def two_num(x, y):
    start_time = time.time()
    if ((x == y) or (x + y == 5) or (abs(x - y) == 5)):
        my_bool = True
    else:
        my_bool = False
    end_time = time.time()
    return my_bool, end_time - start_time

print(two_num(5, 5))
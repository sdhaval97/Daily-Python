# Q. To determine the profiling of Python programs

# importing cProfile module
import cProfile

# declaring and running a sample function
# defining sum_two function
def sum_two(x, y):
    sum = x + y

    if (15 <= sum <= 20):
        sum = 20
    else:
        sum
    return sum

cProfile.run('sum_two(10, 5)')

# cProfile is a module that helps us analyze how long every part of a program takes to execute
# after the program is run, cProfile returns a report that tells us 
# how long each function took to run, how many times it was called
# and how long it took on average each time it was called


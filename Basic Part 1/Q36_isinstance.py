# Q. to print sum of 2 objects only if they are integers

# Defining a function add_num that takes in 2 variables
def add_num(x, y):

    # checking if the input arguments are of integer datatypes
    if not (isinstance(x, int) and isinstance(y, int)):
        return "Use integers as input!"
    else:
        return x + y

# calling the function
print(add_num(5, 10))
print(add_num('5', 10))

# Q. Checking if the number is within 100 of 1000 or 2000

#defining a function
def within1000(n):
    return ((abs(1000-n) <= 100) or (abs(2000 - n) <= 100))

print(within1000(2001))

# Within x of y means the difference between x and y should be less than x
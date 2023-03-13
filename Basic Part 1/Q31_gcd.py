# Q. To compute and print gcd of 2 numbers

# Defining the gcd function
def gcd(x, y):

    # declaring a variable gcd = 1
    gcd = 1

    # if x is completely divisible by y, y is the gcd
    if (x % y == 0):
        return y
    for k in range(int(y/2), 0, -1):
        if ((x % k == 0) and (y % k == 0)):
            gcd = k
            break
    
    return gcd

# printing out the gcd
print(f"GCD of 4 and 6 is {gcd(4, 6)}")
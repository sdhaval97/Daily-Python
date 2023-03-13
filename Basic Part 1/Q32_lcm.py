# Q. computing and printing out the lcm of 2 numbers

# Defining the function lcm that takes in 2 numbers
def lcm(x, y):
    
    # checking if x greater than y and assigning it to z
    if x > y:
        z = x
    else:
        z = y
    
    # initializing a loop to check if z is completely divisible by x or y
    while(True):
        if ((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm

print(lcm(4, 6))
# Q. computing the sum of 3 integers and returning 0 if either of them is equal

def sum_three(x, y, z):
    if ((x == y) or (y == z) or (x == z)):
        sum = 0
    else:
        sum =  x + y + z
    return sum

print(sum_three(4, 6, 7))
print(sum_three(4, 6, 6))
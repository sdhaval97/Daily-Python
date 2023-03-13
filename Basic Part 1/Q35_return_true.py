# Q. returning true if 2 numbers are equal or their sum/diff is 5

# defining the function
def two_num(x, y):
    if ((x == y) or (x + y == 5) or (abs(x - y) == 5)):
        my_bool = True
    else:
        my_bool = False
    return my_bool

print(two_num(5, 5))
print(two_num(2, 3))
print(two_num(5, 10))
print(two_num(3, 7))
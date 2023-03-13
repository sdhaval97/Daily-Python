# Q. Computing sum of 2 numbers and if sum is between 15 and 20 returning 20 as sum

# defining sum_two function
def sum_two(x, y):
    sum = x + y

    if (15 <= sum <= 20):
        sum = 20
    else:
        sum
    return sum

print(sum_two(4, 6))
print(sum_two(10, 6))
print(sum_two(10, 7))
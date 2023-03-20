# Q. To find the sum of n positive numbers

# Asking the users to enter a number
n = int(input("Enter the number of positive numbers you want to get the sum of: "))

# Computing the sum of n positive integers
count = 0
for i in range(1, n+1):
    count += i

print(f"The sum of first {n} numbers is {count}!")

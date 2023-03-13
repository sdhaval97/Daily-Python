# Q. To check whether number is in the list

# importing random to create a list of random integers
import random

# creating a list of 10 random numbers from 1 to 10
randomlist = []
for i in range(0, 10):
    n = random.randint(1, 10)
    randomlist.append(n)

# Asking the user to enter a number
user_number = int(input("Enter a number: "))

# Checking if the input is in the random number list
bool = True
if user_number in randomlist:
    print(bool)
else:
    bool = False
    print(bool)



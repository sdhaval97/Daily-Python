# Q. To calculate the sum of digits of a number

# ASking the user to put in a number
user_number = input("Enter a number: ")

# declaring a counter 
counter = 0

# counting the number of digits using a for loop

# This loop starts from 1 and goes till the length of the user input
for i in range(1, len(user_number)+1):
    counter += 1

print(f"The number of digits is {counter}")



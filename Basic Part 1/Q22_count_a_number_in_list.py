# Q. Counting the instances of a number in python

# Asking the user to enter a list of number between 1 to 10
user_input = input("Enter a list of 20 numbers from 1 to 10: ").split(',')

# Converting the user input to a list
user_list = list(user_input)

# Asking the user the number he wants the instances of
user_number = int(input("Enter the number for which you want the instances: "))

# Counting the number

#Declaring a counter
counter = 0
for number in user_list:
    if int(number) == user_number:
        counter += 1
    else:
        continue

print(f"The number {user_number} has occured in the list {counter} times")
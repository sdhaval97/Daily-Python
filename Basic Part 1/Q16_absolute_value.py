# Q. Printing out the absolute value

# Taking an input from the user
user_input = int(input("Enter a number: "))

# Checking if the number is less than 17, then printing out the difference
# if greater, then printing out twice the absolute difference
if user_input < 17:
    print(f"The difference is: {17 - user_input}")
else:
    print(f"The required output is: {2 * abs(17 - user_input)}")
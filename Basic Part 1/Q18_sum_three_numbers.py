# Q. Returning the sum of 3 numbers

# Taking 3 numbers as input
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# checking if they are equal
# if yes, then printing out thrice the sum

if number1 == number2 == number3:
    print(f"The output is {3 * (number3 + number1 + number2)}")
else:
    print(f"The sum is {number1 + number2 + number3}")
    
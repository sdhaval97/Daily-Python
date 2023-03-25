# Q. To sort the numbers

# Asking the user to put in 3 numbers
number_one = int(input("Enter the 1st number: "))
number_two = int(input("Enter the 2nd number: "))
number_three = int(input("Enter the 3rd number: "))

# sorting out the numbers
a = min(number_one, number_two, number_three)
b = max(number_one, number_two, number_three)
c = (number_one + number_two + number_three) - (a + b)

#printing out the results
print(f"The sorted numbers are {a}, {c}, {b}.")
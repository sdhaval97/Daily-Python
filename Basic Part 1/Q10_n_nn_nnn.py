# Q. taking integer as an input and printing out n + nn + nnn

# Taking in the input
user_input = input('Enter a number: ')

# computing the expression
equation = int(user_input) + int(user_input+user_input) + int(user_input+user_input+user_input)

print(f"The final output is {equation}")
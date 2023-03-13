# Q. Returning first 2 characters of a string

# Asking the user to enter a string
user_string = input("Enter a string: ")

# Asking the user for a number
user_number = int(input("Enter a number: "))

# Logic:
# Multiplying first 2 characters of string by number
# If string is less than 2 characters long, multiplying the full string
if len(user_string) <= 2:
    print(user_string * user_number)
else:
    print(user_string[:2] * user_number)
    

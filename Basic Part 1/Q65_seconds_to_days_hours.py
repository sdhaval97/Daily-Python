# Q. To convert the seconds into days, houra and minutes

# Asking the user to put in the number of seconds
user_input = float(input("Enter the number of seconds: "))

# Converting the seconds to days, hours, and minutes

# We use the floor division method to divide and round the number of days to the closest integer
# We then do a modulo division to work on the remaining number of seconds
days = int(user_input // (3600 * 24))
user_input %= (3600 * 24)

hours = int(user_input // 3600)
user_input %= 3600

minutes = int(user_input // 60)
user_input %= 60

seconds = int(user_input)

print(f"The time is {days}:{hours}:{minutes}:{seconds}")
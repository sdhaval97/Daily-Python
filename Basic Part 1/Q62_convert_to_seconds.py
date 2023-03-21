# Q. Convert all units of time to seconds

# Asking user for the number of days, hours, minutes and seconds
days = int(input("Enter the number of days: "))

hours = int(input("Enter the number of hours: "))

minutes = int(input("Enter the number of minutes: "))

seconds = int(input("Enter the number of seconds: "))

# Converting all the units to seconds
time_in_seconds = (days * 3600 * 24) + (hours * 3600) + (minutes * 60) + seconds

print(f"The time in seconds is {time_in_seconds}")

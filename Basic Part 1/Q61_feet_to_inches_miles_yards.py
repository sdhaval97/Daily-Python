# Q. To convert the distance in feet to inches, yards and miles

# Asking the user to enter the distance in feet
dist_in_feet = float(input("Enter the distance in feet: "))

# Converting the distance in feet to inches, yards, and miles
dist_in_inches = dist_in_feet * 12

dist_in_yards = dist_in_feet * 0.33

dist_in_miles = dist_in_feet * 0.0002

# Printing out the results
print(f"The distance in feet is {dist_in_feet}")
print(f"The corresponding distance in inches is {dist_in_inches}")
print(f"The corresponding distance in yards is {dist_in_yards}")
print(f"The corresponding distance in miles is {dist_in_miles}")

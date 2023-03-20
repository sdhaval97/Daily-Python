# Q. To convert height from feet and inches to centimeter

# Asking the user for their height in feet and then inches
height_in_feet = int(input("Enter your height in feet: "))
height_in_inches = int(input("Enter the inches on top: "))

print(f"The height you entered is {height_in_feet} feet and {height_in_inches} inches!")

# Converting to centimeter
feet_to_cm = height_in_feet * 30.48
inch_to_cm = height_in_inches * 2.54

height_in_cm = feet_to_cm + inch_to_cm

print(f"Your height in centimeters is {height_in_cm}!")

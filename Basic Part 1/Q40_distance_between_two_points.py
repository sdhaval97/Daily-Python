# Q. Computing and printing out the distance between 2 points

# Asking the user to enter the coordinates of the 2 points
x1 = int(input("Enter the x co-ordinate of the 1st point: "))
y1 = int(input("Enter the y co-ordinate of the 1st point: "))
x2 = int(input("Enter the x co-ordinate of the 2nd point: "))
y2 = int(input("Enter the y co-ordinate of the 2nd point: "))

# Computing the distance between the 2 points
distance_between = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

print(f"The distance between the 2 points is: {round(distance_between, 2)}")
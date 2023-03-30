# Q. To determine the midpoints of a line

# Asking the coordinates of the line to the user
x1 = int(input("Enter the x co-ordinate of the 1st point: "))
y1 = int(input("Enter the y co-ordinate of the 1st point: "))

x2 = int(input("Enter the x co-ordinate of the 2nd point: "))
y2 = int(input("Enter the y co-ordinate of the 2nd point: "))

# computing the midpoint co-ordinates of the line
x_mid = (x1 + x2)/2
y_mid = (y1 + y2)/2

print(f"The midpoint of the line lies at ({x_mid}, {y_mid}).")

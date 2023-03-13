# Q. To calculate the volume of sphere

# taking the radius input from the user
radius = int(input("Enter the radius: "))

# declaring constant PI
PI = 3.14

# computing the volume
volume = round(((4/3) * PI * radius ** 3), 2)

print(f"The volume of the sphere with radius {radius} units is {volume} cu. units")
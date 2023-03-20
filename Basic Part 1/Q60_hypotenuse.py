# Q. To calculate the hypotenuse of a right-angled triangle

# Taking in the user input for base and height
height = int(input("Enter the height of the triangle: "))


base = int(input("Enter the base of the triangle: "))


# Computing the hypotenuse
hypotenuse = ((base ** 2) + (height ** 2)) ** 0.5

print(f"The height of the triangle is {height} units!")
print(f"The base of the triangle is {base} units!")
print(f"The hypotenuse of the right-triangle is {hypotenuse} units!")

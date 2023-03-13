# Q. print out the colors in set1 not present in set2

# Declaring 2 color sets
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# Declaring an empty set
color_set = set()

# checking if color in color list 1 is in color list 2

# iterating through color list 1
for color in color_list_1:
    if color not in color_list_2:
        color_set.add(color)

# Printing out the color set
print(color_set)
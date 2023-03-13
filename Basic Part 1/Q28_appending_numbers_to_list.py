# Q. Printing even numbers belonging to a list and stopping after 237

# Declaring a sample list
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

# Declaring an empty list
final_list = []

# Iterating through the numbers list to add even numbers to empty list
for number in numbers:
    if (number % 2 == 0):
        final_list.append(number)
        continue
    elif (number == 237):
        break

print(final_list)
# Q. Creating a histogram of a list of integers

# defining the function histogram
def histogram(numbers):
    
    # for loop to loop through the list of numbers
    for number in numbers:

        # declaring a blank string
        hist = ""
        iteration = number

        # declaring a loop to print the histogram pattern
        while (iteration > 0):
            hist += '*'
            iteration -= 1
        print(hist)

# invoking histogram
histogram([2, 4, 6, 8, 1, 3, 5])

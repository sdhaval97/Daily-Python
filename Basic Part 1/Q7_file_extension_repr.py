#Q. To ask the user for the file name and then print out the extension

# Asking the user for the file name
file_name = input("Enter a file name: ")

# Splitting the filename using the dot as the delimiter
# This gives us a list of 2 elements ['file name', 'extension']
file_split = file_name.split('.')

# Extension is the last element of the file_split list
file_extension = file_split[-1]

# Printing out the printable version of the extension
print(f'The file extension is {repr(file_extension)}')

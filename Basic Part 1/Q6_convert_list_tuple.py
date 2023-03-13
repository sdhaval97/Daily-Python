#Q. Accept a list of comma separated numbers and return as list and tuple

#Asking the user for the input
user_input = input("Enter a series of numbers separated by a comma: ").split(',')

# Converting the series into a list and printing it out
lst_input = list(user_input)
print(lst_input)

# Converting the series into a tuple and printing it out
tpl_input = tuple(user_input)
print(tpl_input)
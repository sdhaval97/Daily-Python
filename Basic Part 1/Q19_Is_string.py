# Q. Checking if string has "Is" and returning the string

# Taking in an input
user_string = input("Enter a word: ")

#Checking if the word starts with Is
if user_string[:2] == "Is":
    print("The string is: " + user_string)
else:
    print("The string is: " + "Is"+user_string)


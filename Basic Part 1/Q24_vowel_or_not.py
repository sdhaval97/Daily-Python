# Q. To check if letter is vowel or not

# Ask user to enter a letter
user_letter = input("Enter a letter: ").upper()

# Creating a list of vowels
vowels = ['A', 'E', 'I', 'O', 'U']

# Checking if user input is a vowel
if user_letter in vowels:
    print(f"The letter {user_letter} is a vowel")
else:
    print(f"The letter {user_letter} is a consonant")

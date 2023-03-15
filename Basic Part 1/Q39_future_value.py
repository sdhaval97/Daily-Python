# Q. Computing and printing out the future value

# Asking the user to input the parameters
principal_amount = int(input("How much money do you want to invest: $"))
rate_of_interest = float(input("What is your expected rate of interest: "))
years = int(input("For how many years do you wish to invest: "))

# computing and printing out future value
future_value = principal_amount * ((1 + (0.01 * rate_of_interest))** years)

print(f"The future value of your invested amount compunded annually is: ${round(future_value, 2)}")

# Q. To calculate the BMI of the body

# Asking the user if they want to put their weight in kgs or lbs
weight_unit = input("Choose the unit you'd like to use for your weight (kg/lb): ").lower()
weight = float(input("Enter the weight: "))

# computing bmi is weight in kgs
if weight_unit == "kg":
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print(f"Your bmi is {round(bmi, 2)}")
# computing bmi if weight in pounds
else:
    height_feet = float(input("Enter your height in feet: "))
    height_inches = float(input("Enter the inches on top: "))
    total_height_in_inches = (height_feet * 12) + (height_inches)
    bmi = (weight * 703) / (total_height_in_inches ** 2)
    print(f"Your bmi is {round(bmi, 2)}") 

# Q. Converting pressure in kPa to other pressure units

# Asking the user to put in the pressure in kilo pascals
pressure_pascals = float(input("Enter the pressure in kilo pascals (kPa): "))

# converting from kPa to lb/sq.inches
pressure_one = pressure_pascals * 0.145

# converting from kPa to mmHg
pressure_two = pressure_pascals * 7.5

# converting from kPa to atmosphere pressure
pressure_three = pressure_pascals * 0.0098

print(f"The pressure in pounds per square inches is {round(pressure_one, 2)}")
print(f"The pressure in mmHg is {round(pressure_two, 2)}")
print(f"The pressure in standard atmosphere pressure is {round(pressure_three, 4)}")
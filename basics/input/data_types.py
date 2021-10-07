name = input("What is your name human? \n")

age = input("How old are you (in years)? \n")

weight = input("How tall are you (in meters)? \n")

height = input("How much do you weigh (in kilograms)?\n")

bmi = float(weight) / float(height**2)

print(f" {name} you are {age} years old and your bmi is {bmi}")
name = input("What is your name human?\n")
age = input("How old are you (in years)?\n")
height = input("How tall are you (in meters)?\n")
weight = input("How much do you weigh (in kilograms)?\n")

bmi = float(weight) / float(height) ** 2

print(f"{name} you are {age} years old and your bmi is {str(bmi)}")

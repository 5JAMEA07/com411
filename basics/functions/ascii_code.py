print("Program Started!")
letter = input("Please enter a standard character:\n")

if len(letter) == 1:
    value = ord(letter)
    print(f"The ASCII code for {letter} is {value}")
else:
    print("invalid input, please insert aa single character")

print("Program Ended!")

print("Program Started!")
code = abs(int(input("Please enter a ASCII code:\n")))

if code in range(32, 127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print("invalid input, please insert a number between the range")

print("Program Ended!")
number = int(input("How many mountains should I display?\n"))
print("Displaying...")

display = "\t__\n       /  \_ \n      /^    \\\n     /  ^    \_\n    _/ ^ ^     ^\\\n   /  ^     ^    \\"

for _ in range(number):
    print(display)

print("Done!")

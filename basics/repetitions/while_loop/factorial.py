number = int(input("Please enter a number?\n"))

counter = 1
final= 1

while counter <= number:
    final *= counter
    counter += 1

print(final)
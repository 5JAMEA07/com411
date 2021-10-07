first_number = input("Please enter the first number.\n")
second_number = input("Please enter the second number.\n")
third_number = input("Please enter the third number.\n")

even_number = 0
odd_number = 0

if int(first_number) % 2 != 0:
    odd_number += 1
else:
    even_number += 1

if int(second_number) % 2 != 0:
    odd_number += 1
else:
    even_number += 1

if int(third_number) % 2 != 0:
    odd_number += 1
else:
    even_number += 1

print(f"There were {even_number} even and {odd_number} odd numbers.")
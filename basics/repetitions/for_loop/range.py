level = int(input("What level of brightness is required?\n"))

display = "*"
print("Adjusting brightness...\n")

for num in range(2, level+2, 2):
    print(f"Beep's brightness level: {display * num}")
    print(f"Bop's brightness level: {display * num}\n")

print("Adjustments complete!")
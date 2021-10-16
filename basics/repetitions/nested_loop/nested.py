rows = int(input("How many rows should I have?\n"))
columns = int(input("How many columns should I have?\n"))

display = ":-)"

print("Here I go:\n")

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(f"{display}", end="")
    print()

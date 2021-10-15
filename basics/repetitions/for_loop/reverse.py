phrase = input("What phrase do you see?\n")

print("Reversing...")
final = ""
for data in range(len(phrase) - 1, -1, -1):
    final += phrase[data]

print(f"The phrase is: {final}")

sequence = input("Please enter a sequence \n")
marker = input("Please enter the character for the marker\n")

final = 0

for character in range(0, len(sequence), 1):
    if marker == sequence[character]:
        loop = character + 1
        while marker != sequence[loop]:
            loop += 1
            final += 1
        break

print(f"The distance between the markers is {final}")

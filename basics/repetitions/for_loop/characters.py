message = input("What strange markings do you see?\n")

print("identifying...")

for word in range(0, len(message), 1):
    print(f" index {word}: {message[word]}")

print("Done!")
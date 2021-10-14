steps = int(input("How far are we from the cave?\n"))

for num in range(steps, 0, -1):
    print(f"{num} steps remaining")

print("We have reached the cave!")
cable = int(input("How many live cables must I avoid?\n"))

avoided_cable = 0
while avoided_cable != cable:
    print("Avoiding...")
    avoided_cable += 1
    print(f"Done! { avoided_cable } live cables avoided")
print("All live cables have been avoided.")

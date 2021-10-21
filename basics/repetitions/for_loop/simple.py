number = int(input("How many mountains should I display?\n"))
print("Displaying...")

display = """__
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\"""

for _ in range(number):
    print(display)

print("Done!")

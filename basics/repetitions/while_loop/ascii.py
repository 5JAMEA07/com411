bar = int(input("How many bars should be charged?\n"))

bar_symbol = "█ "
charged_bar = 0
while charged_bar != bar:
    print("charging...")
    charged_bar += 1
    print(f"{bar_symbol * charged_bar}")
print("The battery is fully charged.")
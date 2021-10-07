lives = input("Please enter the number of lives.\n")
energy = input("Please enter the energy level.\n")
shield = input("Please enter the shield level.\n")

lives_symbol = "♥"
energy_symbol = "♦"
shield_symbol = "♦"

print("\nHealth has been checked\n")
print(f"Lives: {lives_symbol * int(lives)}")
print(f"energy: {energy_symbol * int(energy)}")
print(f"shield: {shield_symbol * int(shield)}")

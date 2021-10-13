user_Number = int(input("How many numbers should I sum up?\n"))

counter = 1
final = 0

while counter <= user_Number:
    sub_user_Number = int(input(f"Please enter number { counter} of {user_Number}:\n"))
    final += sub_user_Number
    counter += 1

print(f"The answer is {final}")

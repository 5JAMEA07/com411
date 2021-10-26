import random

min_num = int(input("Please enter the minimum value:\n"))
max_num = int(input("Please enter the maximum value:\n"))

ran_num = random.randrange(min_num, max_num, 1)

guess = int(input(f"I am thinking of a number between {min_num} and {max_num}.  Can you guess what it is?\n"))

while guess != ran_num:
    if guess > ran_num:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    another = int(input("Try again:\n"))
    guess = another


print("Congratulations! You guessed my number!")
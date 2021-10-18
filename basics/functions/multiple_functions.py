display = """| |
***"""


def display_ladder(steps):
    for steps in range(0, steps, 1):
        print(display)


def create_ladder():
    number = int(input("How many steps remain?\n"))
    display_ladder(number)


create_ladder()
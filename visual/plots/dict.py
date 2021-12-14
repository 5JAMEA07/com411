import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}
    line = input("what type of line would you like\n")
    colour = input("what type of color would you like\n")
    marker = input("What style of marker would you like\n")

    paths["line"] = line
    paths["colour"] = colour
    paths["marker"] = marker
    return paths


def generate():
    print("How many lines would you like to display?")
    loop = int(input())
    for _ in range(0, loop):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        param = f"{values['colour']}{values['line']}{values['marker']}"
        plt.plot(x, y, param)
        plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


run()

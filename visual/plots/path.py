import matplotlib.pyplot as plt


def coordinate():
    x = input("enter an x value \n")
    y = input("enter an y value \n")

    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for item in range(0, 4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return x_values, y_values


def run():
    values = path()
    x = values[0]
    y = values[1]
    plt.plot(x, y, 'r--o')
    plt.show()


run()

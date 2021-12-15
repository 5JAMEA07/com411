import matplotlib.pyplot as plt


def read_data(path_name):
    temp = []
    with open(path_name) as file:
        for data in file:
            temp.append(int(data.strip()))

    return temp


def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2, sharey="row")
    x = range(1, 8)
    y = data
    axs[0].plot(x, y)
    axs[1].bar(x, y)
    # set x limits to show all days
    axs[0].set_xlim(min(x), max(x))
    axs[1].set_xlim(min(x), max(x))

    # add labels
    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Temperature")
    axs[1].set_xlabel("Day")
    # Note, no y-label needed for second subplot as the y-axis is shared

    plt.tight_layout()
    plt.show()


run()

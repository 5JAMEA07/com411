import csv

import matplotlib.pyplot as plt


def read_data():
    with open("temps.csv") as file:
        csv_reader = csv.reader(file)
        heading = next(csv_reader)
        plot_data = {heading[0]: [], heading[1]: []}

        for data in csv_reader:
            plot_data[heading[0]].append(int(data[0]))
            plot_data[heading[1]].append(int(data[1]))

        return plot_data


def run():
    data = read_data()
    print(data)
    fig, ax = plt.subplots(2, 1, sharex="row")
    ax[0].plot(range(1, 8), data["week1"])
    ax[1].plot(range(1, 8), data["week2"])
    plt.tight_layout()
    plt.show()


run()

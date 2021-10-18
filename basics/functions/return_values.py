def sum_weights(bot1, bot2):
    return bot1 + bot2


def calc_avg_weight(bot1, bot2):
    return sum_weights(bot1, bot2)/2


def run():
    bot1 = int(input("What is the weight of Beep?\n"))
    bot2 = int(input("What is the weight of Bop?\n"))

    data = input("What would you like to calculate (sum or average)?\n")
    if data == "sum":
        result = sum_weights(bot1, bot2)
        print(f"The sum of Beep and Bop's weight is {result}.")
    elif data == "average":
        result = calc_avg_weight(bot1, bot2)
        print(f"The average of Beep and Bop's weight is {result}")


run()

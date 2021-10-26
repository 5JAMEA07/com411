def export(file_path, num_of_bot):
    print("Exporting...")
    with open(file_path, "a") as file:
        for num in range(0, num_of_bot, 1):
            bot_id = input("Please enter the bot id:\n")
            bot_name = input("Please enter the bot name:\n")
            bot_paint = input("Please enter the bot paint:\n")
            file.write(f"\n{bot_id},{bot_name},{bot_paint}")
    print("Done!")


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
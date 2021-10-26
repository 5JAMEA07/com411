import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        city_name = data["city"]
        print(f"City Name: {city_name}")
        population = data["population"]
        print(f"Population Size: {population}")
        bots = data["bots"]
        for bot in bots:
            name = bot["name"]
            strength = bot["stats"]["strength"]
            speed = bot["stats"]["speed"]
            stats = f"has a strength level of {strength} and a speed level of {speed}."
            print(f"{name} has the following stats: {stats}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()

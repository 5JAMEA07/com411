def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)


def display_values(data):
    print("values:")
    for value in data.values():
        print(value)


def display_items(data):
    print("pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


run()

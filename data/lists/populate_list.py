def directions():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction


def menu():
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")
    choice = int(input())
    return direction[choice]


def run():
    route = []
    print("Working out escape route...\n")
    print("Please enter a direction:")
    for _ in range(5):
        data = menu()
        route.append(data)
    print(f"Escape route: {route}")



if __name__ == "__main__":
    run()

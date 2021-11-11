def observed():
    observations = []
    for _ in range(5):
        data = input("Please enter an observation:\n")
        observations.append(data)
    return observations


def remove_observations(observations):
    option = input("Do you wish to remove an observation (yes/no)?\n")
    while option == "yes":
        delete = input("What observation do you wish to remove?\n")
        observations.remove(delete)
        print("Done!")
        option = input("Do you wish to remove an observation (yes/no)?\n")
    return observations


def run():
    observations = observed()
    data = remove_observations(observations)
    other = set()
    for item in data:
        count = data.count(item)
        tuple_add = (item, count)
        other.add(tuple_add)
    print("")
    others = sorted(other)
    print("Observations:")
    for sets in others:
        print(f"{sets[0]} observed {sets[1]} times")


run()

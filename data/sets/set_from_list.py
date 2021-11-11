def observed():
    observations = []
    for _ in range(3):
        data = input("Please enter an observation:\n")
        observations.append(data)
    return observations


def run():
    print("Counting observations...")
    data = observed()
    other = set()
    for item in data:
        count = data.count(item)
        tuple_add = (item, count)
        other.add(tuple_add)
    print("")
    for sets in other:
        print(f"{sets[0]} observed {sets[1]} times")


run()

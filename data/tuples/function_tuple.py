def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    data = likelihood()
    print(f"Minimum likelihood of falling: {data[0]}%")
    print(f"Maximum likelihood of falling: {data[1]}%")


if __name__ == "__main__":
    run()

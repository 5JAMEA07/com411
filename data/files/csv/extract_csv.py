import csv


def extract(file_path):
    print("Extracting...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = "\n"
        for name in csv_reader:
            names += f"{name[1]} \n"
        print(f"Done! \nThe extracted names are as follows: {names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()

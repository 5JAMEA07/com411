import os


def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    files = os.listdir(path)
    for file in files:
        print(file)


def run():
    print("Processing...")
    cwd()


run()

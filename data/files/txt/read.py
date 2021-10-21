def display_chars(file_name, num_char):
    with open(file_name) as file:
        data = file.read(num_char)
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline()
        print(data)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()

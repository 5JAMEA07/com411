def search(file_path):
    print("searching...")
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            check = line[0:7]
            if check == "Section":
                sections += f"{line.strip()}\n"
            else:
                books += f"{line.strip()}\n"
    return f"{sections}\n\n{books}"


def save(file_path, data):
    print("saving")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")


def run():
    data = search("books.txt")
    save("section-books.txt", data)


if __name__ == "__main__":
    run()

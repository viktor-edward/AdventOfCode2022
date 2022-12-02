def readFile(fileInput):
    data = []
    with open(fileInput, "r") as file:
        for line in file.readlines():
            data.append(int(line.replace("\n", "")))
    return data


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")

    print("Part two: ")


if __name__ == '__main__':
    main()

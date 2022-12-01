def readFile(fileInput):
    data = []
    with open(fileInput, "r") as file:
        for line in file.readlines():
            data.append(int(line.replace("\n", "")))
    return data


def func1(data):
    return 0


def func2(data):
    return 0


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")

    print("Part two: ")


if __name__ == '__main__':
    main()

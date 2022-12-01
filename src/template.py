import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    with open(fileInput, "r") as file:
        for line in f.readlines():
            data.append(int(line.replace("\n", "")))
    return data


def func1(data):
    return 0


def func2(data):
    return 0


def main():
    data = readFile("../resources/day2_input.txt")

    print("Part one: ")

    print("Part two: ")


if __name__ == '__main__':
    main()

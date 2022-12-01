def readFile(fileInput):
    data = []
    tempSum = 0
    with open(fileInput, "r") as file:
        for line in file.readlines():
            if "\n" == line:
                data.append(tempSum)
                tempSum = 0
            else:
                tempSum += int(line.replace("\n", ""))
        data.append(tempSum)
    return data


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")
    print(max(data))

    print("Part two: ")
    data.sort(reverse=True)
    print(sum(data[0:3]))


if __name__ == '__main__':
    main()

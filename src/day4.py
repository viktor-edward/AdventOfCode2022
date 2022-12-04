def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as file:
        for line in file.readlines():
            data.append(list(map(int, line.replace("\n", "").replace("-", ",").split(","))))
    return data


def main():
    data = readFile("../resources/day4_input.txt")

    print("Part one: ")
    overlappingSections = 0
    for assignmentPair in data:
        if assignmentPair[0] >= assignmentPair[2] and assignmentPair[1] <= assignmentPair[3]:
            overlappingSections += 1
        elif assignmentPair[0] <= assignmentPair[2] and assignmentPair[1] >= assignmentPair[3]:
            overlappingSections += 1
    print(f"There are {overlappingSections} overlapping assigned sections.")

    print("\nPart two: ")
    overlappingSections = 0
    for assignmentPair in data:
        if assignmentPair[0] <= assignmentPair[2] <= assignmentPair[1]:
            overlappingSections += 1
        elif assignmentPair[0] <= assignmentPair[3] <= assignmentPair[1]:
            overlappingSections += 1
        elif assignmentPair[2] <= assignmentPair[0] <= assignmentPair[3]:
            overlappingSections += 1
        elif assignmentPair[2] <= assignmentPair[1] <= assignmentPair[3]:
            overlappingSections += 1
    print(f"There are {overlappingSections} sections that are overlapping in at least a single section.")


if __name__ == '__main__':
    main()

def readFile(fileInput):
    data = []
    with open(fileInput, "r") as file:
        for line in file.readlines():
            data.append(line.replace("\n", ""))
    return data


def getPriority(item: str) -> int:
    if item.isupper():  # ord("A") = 65
        return ord(item) - 64 + 26
    else:  # ord("a") = 97
        return ord(item) - 96 + 0


def main():
    data = readFile("../resources/day3_input.txt")

    commonItems = []
    print("Part one: ")
    for rucksack in data:
        amountOfItems = len(rucksack)
        firstCompartment, secondCompartment = rucksack[:amountOfItems//2], rucksack[amountOfItems//2:]
        tempSet = set()
        for item in firstCompartment:
            if item in secondCompartment:
                tempSet.add(item)
        for item in tempSet:
            commonItems.append(item)
    totalPriority = sum(getPriority(x) for x in commonItems)
    print(f"Total priority is {totalPriority}. \n")

    print("Part two: ")
    priorityBadges = []
    for i in range(len(data)//3):
        rucksack1, rucksack2, rucksack3 = data[(i - 1)*3], data[(i - 1)*3 + 1], data[(i - 1)*3 + 2]
        tempSet = set()
        for item in rucksack1:
            if item in rucksack2:
                if item in rucksack3:
                    tempSet.add(item)
        for item in tempSet:
            priorityBadges.append(item)
    totalBadgePriority = sum(getPriority(x) for x in priorityBadges)
    print(f"Total priority for the badges is {totalBadgePriority}. \n")


if __name__ == '__main__':
    main()

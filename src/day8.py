def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            data.append(line.replace("\n", ""))
    return data


def isTreeVisible(x: int, y: int, forest: list) -> bool:
    treeHeight = int(forest[y][x])
    if x == 0 or y == 0 or x == len(forest[0]) - 1 or y == len(forest) - 1:
        return True
    for i in range(x):
        if int(forest[y][i]) >= treeHeight:
            break
        elif i == x - 1:
            return True
    for i in range(x + 1, len(forest[y])):
        if int(forest[y][i]) >= treeHeight:
            break
        elif i == len(forest[y]) - 1:
            return True
    for i in range(y):
        if int(forest[i][x]) >= treeHeight:
            break
        elif i == y - 1:
            return True
    for i in range(y + 1, len(forest)):
        if int(forest[i][x]) >= treeHeight:
            break
        elif i == len(forest) - 1:
            return True
    return False


def calculateScenicScore(x: int, y: int, forest: list) -> int:
    scenicScore = 1
    treeHeight = int(forest[y][x])
    tempScenicScore = 0
    for i in reversed(range(x)):
        tempScenicScore += 1
        if int(forest[y][i]) >= treeHeight:
            break
    scenicScore *= tempScenicScore
    tempScenicScore = 0
    for i in range(x + 1, len(forest[y])):
        tempScenicScore += 1
        if int(forest[y][i]) >= treeHeight:
            break
    scenicScore *= tempScenicScore
    tempScenicScore = 0
    for i in reversed(range(y)):
        tempScenicScore += 1
        if int(forest[i][x]) >= treeHeight:
            break
    scenicScore *= tempScenicScore
    tempScenicScore = 0
    for i in range(y + 1, len(forest)):
        tempScenicScore += 1
        if int(forest[i][x]) >= treeHeight:
            break
    scenicScore *= tempScenicScore
    return scenicScore


def main():
    forest = readFile("../resources/day8_input.txt")

    print("Part one: ")
    visibleTrees = 0
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if isTreeVisible(j, i, forest):
                visibleTrees += 1
    print(visibleTrees)

    print("\nPart two: ")
    bestScenicScore = 0
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            scenicScore = calculateScenicScore(j, i, forest)
            if bestScenicScore < scenicScore:
                bestScenicScore = scenicScore
    print(bestScenicScore)


if __name__ == '__main__':
    main()

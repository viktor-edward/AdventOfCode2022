from collections import defaultdict


def readFile(fileInput):
    data = []
    with open(fileInput, "r") as file:
        for line in file.readlines():
            data.append((line.replace("\n", "").split(" ")))
    return data


def setScores() -> defaultdict:
    scores = defaultdict(dict)
    scores["A"]["X"] = 3 + 1
    scores["A"]["Y"] = 6 + 2
    scores["A"]["Z"] = 0 + 3
    scores["B"]["X"] = 0 + 1
    scores["B"]["Y"] = 3 + 2
    scores["B"]["Z"] = 6 + 3
    scores["C"]["X"] = 6 + 1
    scores["C"]["Y"] = 0 + 2
    scores["C"]["Z"] = 3 + 3
    return scores


def setAction() -> defaultdict:
    action = defaultdict(dict)
    action["A"]["X"] = "Z"
    action["A"]["Y"] = "X"
    action["A"]["Z"] = "Y"
    action["B"]["X"] = "X"
    action["B"]["Y"] = "Y"
    action["B"]["Z"] = "Z"
    action["C"]["X"] = "Y"
    action["C"]["Y"] = "Z"
    action["C"]["Z"] = "X"
    return action


def main():
    scores = setScores()
    strategy = readFile("../resources/day2_input.txt")

    print("Part one: ")
    totalScore = 0
    for match in strategy:
        opponent, you = match[0], match[1]
        totalScore += scores[opponent][you]
    print(totalScore)

    print("Part two: ")
    totalScore = 0
    action = setAction()
    for match in strategy:
        opponent, you = match[0], match[1]
        youNew = action[opponent][you]
        totalScore += scores[opponent][youNew]
    print(totalScore)


if __name__ == '__main__':
    main()

import math


def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            data.append(line.replace("\n", ""))
    return data


def newTailPosition(hx, hy, tx, ty):
    if math.sqrt(math.pow(hx - tx, 2) + math.pow(hy - ty, 2)) >= 2:
        if hy - ty > 0:
            ty += 1
        elif hy - ty < 0:
            ty -= 1
        if hx - tx > 0:
            tx += 1
        elif hx - tx < 0:
            tx -= 1
    return tx, ty


def calculateVisitedCells(numOfTails, instructions):
    hx, hy, tx, ty = 0, 0, 0, 0
    tails = []
    visitedTailSpots = set()
    visitedTailSpots.add((0, 0))
    for i in range(numOfTails + 1):  # Head = tail[0]
        tails.append((0, 0))
    for instr in instructions:
        direction, steps = instr.split(" ")
        for i in range(int(steps)):
            for tailNr, tail in enumerate(tails):
                if tailNr == 0:  # Update head
                    hx, hy = tail
                    if direction == "U":
                        hy += 1
                    elif direction == "D":
                        hy -= 1
                    elif direction == "R":
                        hx += 1
                    elif direction == "L":
                        hx -= 1
                    tails[tailNr] = (hx, hy)
                else:  # Update tails
                    tx, ty = tail
                    tx, ty = newTailPosition(hx, hy, tx, ty)
                    hx, hy = tx, ty  # new head for next tail
                    tails[tailNr] = (tx, ty)
                if tailNr == numOfTails:
                    visitedTailSpots.add((tx, ty))
    print(len(visitedTailSpots))


def main():
    instructions = readFile("../resources/day9_input.txt")

    print("Part one: ")
    calculateVisitedCells(1, instructions)

    print("\nPart two: ")
    calculateVisitedCells(9, instructions)


if __name__ == '__main__':
    main()

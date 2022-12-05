def readFile(fileInput: str) -> (list, list):
    initialState = []
    instructions = []
    with open(fileInput, "r") as file:
        rows = []
        for line in file.readlines():
            if "[" in line:
                rows.append(line.replace("\n", ""))
            elif line.startswith(" 1"):
                for i, row in enumerate(reversed(rows)):
                    row = row.replace("    ", "[ ").replace("]", "").replace(" ", "").split("[")[1:]
                    for j, block in enumerate(row):
                        if i == 0:
                            initialState.append([block])
                        else:
                            if block != "":
                                initialState[j].append(block)
            elif line.startswith("move"):
                instructions.append(list(map(int, line.replace("move ", "").
                                             replace("from", "to").replace("\n", "").split(" to "))))
    return initialState, instructions


def main():
    print("Part one: ")
    state, instructions = readFile("../resources/day5_input.txt")
    for instr in instructions:
        for x in range(instr[0]):
            state[instr[2] - 1].append(state[instr[1] - 1].pop())
    finalMessage = ""
    for x in state:
        finalMessage += (x[-1])
    print(finalMessage)

    print("\nPart two: ")
    state, instructions = readFile("../resources/day5_input.txt")
    for instr in instructions:
        state[instr[2] - 1] = state[instr[2] - 1] + state[instr[1] - 1][-instr[0]:]
        state[instr[1] - 1] = state[instr[1] - 1][:-instr[0]]
    finalMessage = ""
    for x in state:
        finalMessage += (x[-1])
    print(finalMessage)


if __name__ == '__main__':
    main()

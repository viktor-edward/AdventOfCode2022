def readFile(fileInput: str) -> list:
    with open(fileInput, "r") as file:
        for line in file.readlines():
            return line


def containsDuplicates(strToCheck: str) -> bool:
    uniqueChars = set()
    for x in strToCheck:
        uniqueChars.add(x)
    if len(set(uniqueChars)) == len(strToCheck):
        return False
    else:
        return True


def main():
    signal = readFile("../resources/day6_input.txt")

    print("Part one: ")
    block = signal[:4]
    signal = signal[4:]
    for i, x in enumerate(signal):
        if containsDuplicates(block):
            block = block[1:] + x[0]
        else:
            break
    print(f"First marker {block} found after {i + 4}.")

    print("\nPart two: ")
    signal = readFile("../resources/day6_input.txt")
    block = signal[:14]
    signal = signal[14:]
    for i, x in enumerate(signal):
        if containsDuplicates(block):
            block = block[1:] + x[0]
        else:
            break
    print(f"First marker {block} found after {i + 14}.")


if __name__ == '__main__':
    main()

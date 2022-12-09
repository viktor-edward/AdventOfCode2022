from collections import defaultdict
folders = defaultdict(dict)


def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            data.append(line.replace("\n", ""))
    return data


class folder:
    def __init__(self, name, subFolders=None, fileSize=0):
        if subFolders is None:
            subFolders = set()
        self.name = name
        self.subFolders = subFolders
        self.fileSize = fileSize

    def __str__(self):
        return f"{self.name} contains the folders {self.subFolders} and files with size {self.fileSize}."

    def addSubFolder(self, subFolder):
        self.subFolders.add(subFolder)

    def addFile(self, fileSize):
        self.fileSize += fileSize

    def getSize(self) -> int:
        size = 0
        for sf in self.subFolders:
            size += folders[sf].getSize()
        return size + self.fileSize


def main():
    data = readFile("../resources/day7_input.txt")

    print("Part one: ")
    maxSize = 100000
    folderPath = ["/"]
    folders["/"] = folder("/")
    data = data[1:]
    for row in data:
        row = str(row)
        currentFolder = folderPath[-1]
        if row.startswith("$ cd "):
            path = row[5:]
            if path == "..":
                folderPath.pop()
            else:
                newFolder = currentFolder + path
                folderPath.append(newFolder)
                if newFolder not in folders:
                    folders[newFolder] = folder(newFolder)
                if len(folderPath) > 1:
                    temp = folders[currentFolder]
                    temp.addSubFolder(newFolder)
                    folders[currentFolder] = temp
        elif row.startswith("$ ls") or row.startswith("dir"):
            pass
        else:
            fileSize, fileName = row.split(" ")
            temp = folders[currentFolder]
            temp.addFile(int(fileSize))
            folders[currentFolder] = temp

    subTotal = 0
    for key, f in folders.items():
        folderSize = f.getSize()
        if folderSize < maxSize:
            subTotal += folderSize
    print(subTotal)

    print("\nPart two: ")
    maxSize = 70000000 - 30000000
    minSizeToRemove = folders["/"].getSize() - maxSize
    bestDeletion = maxSize
    for key, f in folders.items():
        folderSize = f.getSize()
        if minSizeToRemove < folderSize < bestDeletion:
            bestDeletion = folderSize
    print(bestDeletion)


if __name__ == '__main__':
    main()

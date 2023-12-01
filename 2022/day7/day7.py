class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

def buildFilesystemTree(lines):
    i = 0
    rootDir = None
    currentDir = None
    for line in lines:
        if line.startswith("$ cd"):
            dirName = line.split(" ")[2].rstrip()
            if dirName == "..":
                currentDir = currentDir.parent
            elif dirName == "/":
                currentDir = Dir(name = dirName, parent = None)
                rootDir = currentDir
            else:
                temp = Dir(name = dirName, parent = currentDir)
                currentDir.children.append(temp)
                currentDir = temp
        elif line[0].isdigit(): 
            size, name = line.rstrip().split(" ")
            currentDir.children.append(File(name, size))
        # we don't actually need to do anything for ls and dir lines, can ignore them.
    return rootDir

def getDirSizes(dir, sizeList):
    size = 0
    for child in dir.children:
        if type(child) is File:
            size += int(child.size)
        else:
            size += getDirSizes(child, sizeList)
    sizeList.append(size)
    return size

## for debugging ##
def printTree(dir, indent):
    print(indent + dir.name)
    for child in dir.children:
        if type(child) is File:
            print(indent + " " + child.name)
        else:
            printTree(child, indent + " ")

## for debugging ##
def shallowPrint(dir):
    for child in dir.children:
        print(child.name)

def part1(lines):
    rootDir = buildFilesystemTree(lines)
    # printTree(rootDir, "")
    sizes = []
    getDirSizes(rootDir, sizes)
    # print(sizes)
    print(sum(filter(lambda x: x <= 100000, sizes)))

def part2(lines):
    rootDir = buildFilesystemTree(lines)
    sizes = []
    getDirSizes(rootDir, sizes)
    spaceNeeded = 30000000 - (70000000 - max(sizes))
    print(min(filter(lambda x: x >= spaceNeeded, sizes)))

with open('input.txt') as f:
    lines = f.readlines()

print("Part 1: ")
part1(lines)
print("\nPart 2: ")
part2(lines)
import os

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def part1(input):
    print("Part 1: ")
    sum = 0
    for line in input:
        firstDigit = ''
        secondDigit = ''
        for c in line:
            if c.isdigit():
                firstDigit = c
                break
        for c in reversed(line):
            if c.isdigit():
                secondDigit = c
                break
        sum = sum + int(firstDigit) * 10 + int(secondDigit)
    print(sum)

def findFirstDigitString(line):
    firstDigit = -1
    firstIndex = 10000
    for i, digit in enumerate(digits):
        index = line.find(digit)
        if index != -1 and index < firstIndex:
            firstIndex = index
            firstDigit = i + 1
    # print((firstIndex, firstDigit))
    return firstIndex, firstDigit

def findLastDigitString(line):
    lastDigit = -1
    lastIndex = -1
    for i, digit in enumerate(digits):
        index = line.rfind(digit)
        if index != -1 and index > lastIndex:
            lastIndex = index
            lastDigit = i + 1
    # print((lastIndex, lastDigit))
    return lastIndex, lastDigit

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for line in input:
        firstIndex, firstDigit = findFirstDigitString(line)
        for i, c in enumerate(line):
            if c.isdigit():
                if firstIndex == -1 or i < firstIndex:
                    firstDigit = int(c)
                    break
        lastIndex, lastDigit = findLastDigitString(line)
        for i, c in enumerate(reversed(line)):
            if c.isdigit():
                if lastIndex == -1 or (len(line)-i) > lastIndex:
                    lastDigit = int(c)
                    break
        val = firstDigit * 10 + lastDigit
        print(val)
        sum = sum + val
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

# part1(input)
part2(input)
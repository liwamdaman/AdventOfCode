from itertools import accumulate

class Monkey:
    def __init__(self, items, operationFunc, testDivisor, trueDestination, falseDestination):
        self.items = items
        self.operationFunc = operationFunc
        self.testDivisor = testDivisor
        self.trueDestination = trueDestination
        self.falseDestination = falseDestination
        self.inspectCount = 0

def parseInput(filename):
    with open(filename) as f:
        lines = f.read().split("\n\n")
        return lines

def parseMonkeys(input):
    monkeys = []
    for monkeyLines in input:
        lines = monkeyLines.split("\n")
        monkeys.append(Monkey(parseItems(lines[1]), parseOperation(lines[2]), parseTest(lines[3]), parseTrueDest(lines[4]), parseFalseDest(lines[5])))
    return monkeys

def parseItems(itemsLine):
    return list(map(int, itemsLine.rstrip().split(": ")[1].split(", ")))

def parseOperation(operationLine):
    expression = operationLine.rstrip().split(" = ")[1]
    _, operator, operand = expression.split(" ")
    if operator == "+":
        if operand.isdigit():
            return lambda x: x + int(operand)
        else:
            return lambda x: x + x
    else:
        if operand.isdigit():
            return lambda x: x * int(operand)
        else:
            return lambda x: x * x

def parseTest(testLine):
    return int(testLine.rstrip().split("divisible by ")[1])

def parseTrueDest(trueDestLine):
    return int(trueDestLine.rstrip().split("monkey ")[1])

def parseFalseDest(falseDestLine):
    return int(falseDestLine.rstrip().split("monkey ")[1])

def runMonkeys(monkeys, numRounds, isPart2=False):
    if isPart2:
        modulus = list(accumulate(list(map(lambda x: x.testDivisor, monkeys)), (lambda x, y: x * y)))[-1] # was just playing with itertools here, awful code
    for round in range(numRounds):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items.pop(0)
                worry = monkey.operationFunc(item)
                if isPart2:
                    worry = worry % modulus
                else:
                    worry = worry // 3
                if worry % monkey.testDivisor == 0:
                    monkeys[monkey.trueDestination].items.append(worry)
                else:
                    monkeys[monkey.falseDestination].items.append(worry)
                monkey.inspectCount += 1

def part1(input):
    print("Part 1: ")
    monkeys = parseMonkeys(input)
    runMonkeys(monkeys, 20)
    monkeys.sort(reverse = True, key = lambda x: x.inspectCount)
    print(monkeys[0].inspectCount * monkeys[1].inspectCount)

def part2(input):
    print("\nPart 2: ")
    monkeys = parseMonkeys(input)
    runMonkeys(monkeys, 10000, True)
    monkeys.sort(reverse = True, key = lambda x: x.inspectCount)
    print(monkeys[0].inspectCount * monkeys[1].inspectCount)

input = parseInput("input.txt")

part1(input)
part2(input)
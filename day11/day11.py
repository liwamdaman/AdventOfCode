class Monkey:
    def __init__(self, items, operationFunc, testFunc, trueDestination, falseDestination):
        self.items = items
        self.operationFunc = operationFunc
        self.testFunc = testFunc
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
    divisibleBy = testLine.rstrip().split("divisible by ")[1]
    return lambda x: (x % int(divisibleBy)) == 0

def parseTrueDest(trueDestLine):
    return int(trueDestLine.rstrip().split("monkey ")[1])

def parseFalseDest(falseDestLine):
    return int(falseDestLine.rstrip().split("monkey ")[1])

def runMonkeys(monkeys):
    for round in range(20):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items.pop(0)
                worry = monkey.operationFunc(item)
                worry = worry // 3
                if monkey.testFunc(worry):
                    monkeys[monkey.trueDestination].items.append(worry)
                else:
                    monkeys[monkey.falseDestination].items.append(worry)
                monkey.inspectCount += 1

def part1(input):
    print("Part 1: ")
    monkeys = parseMonkeys(input)
    runMonkeys(monkeys)
    monkeys.sort(reverse = True, key = lambda x: x.inspectCount)
    print(monkeys[0].inspectCount * monkeys[1].inspectCount)

def part2(input):
    print("\nPart 2: ")

input = parseInput("input.txt")

part1(input)
part2(input)
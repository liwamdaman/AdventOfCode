import ast
import functools

class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return "left: " + str(self.left) + ", right: " + str(self.right)

class Packet:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return str(self.data)

def parseInput(filename):
    with open(filename) as f:
        pairs = f.read().split("\n\n")
        return pairs

def parsePairs(pairs):
    Pairs = []
    for pair in pairs:
        [left, right] = pair.split("\n")
        Pairs.append(Pair(parsePackets(left.rstrip()), parsePackets(right.rstrip())))
    return Pairs
    
def parsePackets(packet):
    # Is using eval cheating????
    data = ast.literal_eval(packet)
    return Packet(data)

def compare(left, right):
    match left, right:
        case int(), int():
            if left < right:
                return 1
            if left == right:
                return 0
            return -1
        case list(), list():
            for i in range(len(right)):
                if i >= len(left):
                    return 1
                result = compare(left[i], right[i])
                if result != 0:
                    return result
            # so far lists have been equal, compared lengths of lists
            if len(left) == len(right):
                return 0
            return -1   # left is longer
        case list(), int():
            return compare(left, [right])
        case int(), list():
            return compare([left], right)

def part1(input):
    print("Part 1: ")
    pairs = parsePairs(input)
    result = 0
    for i, v in enumerate(pairs):
        if compare(v.left.data, v.right.data) == 1:
            result += (i+1)
    print(result)

def part2(input):
    print("\nPart 2: ")
    sortedPackets = []
    for pair in input:
        [left, right] = pair.split("\n")
        sortedPackets.extend([ast.literal_eval(left.rstrip()), ast.literal_eval(right.rstrip())])
    sortedPackets.extend([[[2]], [[6]]])
    sortedPackets.sort(reverse=True, key=functools.cmp_to_key(compare))
    # print(sortedPackets)
    print((1 + sortedPackets.index([[2]])) * (1 + sortedPackets.index([[6]])))


input = parseInput("input.txt")

part1(input)
part2(input)
import os
import re
import sys
import math
sys.setrecursionlimit(1000000)

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def traverse(instructions, map, currInstructionIndex, currNode, isDestFn):
    # print(currNode)
    if isDestFn(currNode):
        return 0
    currInstruction = instructions[currInstructionIndex]
    if currInstruction == 'L':
        currNode = map[currNode][0]
    if currInstruction == 'R':
        currNode = map[currNode][1]
    currInstructionIndex = (currInstructionIndex + 1) % len(instructions)

    return 1 + traverse(instructions, map, currInstructionIndex, currNode, isDestFn)


def part1(input):
    print("Part 1: ")
    instructions = input.pop(0).rstrip()
    input.pop(0)
    map = {}
    for line in input:
        [node, leftRight] = line.split(" = ")
        matches = re.search("\((\w+), (\w+)\)", leftRight)
        left = matches.group(1)
        right = matches.group(2)
        map[node] = (left, right)
    numSteps = traverse(instructions, map, 0, 'AAA', lambda x: x == 'ZZZ')
    print(numSteps)

def part2(input):
    print("\nPart 2: ")
    instructions = input.pop(0).rstrip()
    input.pop(0)
    map = {}
    startNodes = []
    for line in input:
        [node, leftRight] = line.split(" = ")
        matches = re.search("\((\w+), (\w+)\)", leftRight)
        left = matches.group(1)
        right = matches.group(2)
        map[node] = (left, right)
        if node.endswith('A'):
            startNodes.append(node)
    numSteps = []
    for node in startNodes:
        numSteps.append(traverse(instructions, map, 0, node, lambda x: x.endswith('Z')))
    print(math.lcm(*numSteps))

dirname = os.path.dirname(__file__)
filename1 = os.path.join(dirname, 'input.txt')
filename2 = os.path.join(dirname, 'input.txt')
input1 = parseInput(filename1)
input2 = parseInput(filename2)

part1(input1)
part2(input2)
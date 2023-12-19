import sys
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
import utils
import re

import os

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines[0].split(',')
    
def hash(s):
    # print(s)
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    # print(val)
    return val

def part1(input):
    print("Part 1: ")
    sum = 0
    for step in input:
        sum += hash(step)
    print(sum)

def performOperation(label, operation, focalLength, m):
    boxNum = hash(label)
    box = m.get(boxNum, [])
    if operation == '-':
        try:
            index = [i for i,x in enumerate(box) if x[0] == label][0]
            box.pop(index)
        except:
            return
    else:
        try:
            index = [i for i,x in enumerate(box) if x[0] == label][0]
            box[index] = (label, int(focalLength))
        except:
            box.append((label, int(focalLength)))
    m[boxNum] = box

def part2(input):
    print("\nPart 2: ")
    """
    Has schema like:
    {
        0: [('rm',4), ('cu', 7)],
        5: [('xd', 1)]
    }
    """
    m = {}
    for step in input:
        (label, operation, focalLength) = re.search("([a-z]+)(=|-)(\d*)", step).groups()
        performOperation(label, operation, focalLength, m)
    sum = 0
    for boxNum, box in m.items():
        if box:
            for i, lens in enumerate(box):
                # print(boxNum, i, lens)
                sum += (1+boxNum) * (i+1) * lens[1]
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)
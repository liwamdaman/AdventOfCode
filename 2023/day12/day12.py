import sys
sys.path.insert(1, '/Users/willi/adventOfCode/utils')

import os
import re
from utils import timeFunction

# sys.setrecursionlimit(100000000)

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
### PART 1 APPROACH ###
def isPermutationValid(permutation, sizes):
    groups = re.findall('[#]+', permutation)
    # print(groups)
    if len(groups) != len(sizes):
        return False
    for i, group in enumerate(groups):
        if len(group) != sizes[i]:
            return False
    return True

def dfs(record, sizes, idx, currPermutation):
    if idx == len(record):
        # time to check
        return 1 if isPermutationValid(currPermutation, sizes) else 0
    if record[idx] != '?':
        numValid = dfs(record, sizes, idx+1, currPermutation+record[idx])
    else:
        numValid = dfs(record, sizes, idx+1, currPermutation+'#') + dfs(record, sizes, idx+1, currPermutation+'.')
    return numValid
#######################

### PART 2 APPROACH ###
cache = {}
def traverse(record, sizes):
    if record == "":
        return 1 if sizes == () else 0
    if sizes == ():
        return 0 if '#' in record else 1
    
    if (record, sizes) in cache:
        return cache[(record, sizes)]

    numValid = 0
    if record[0] == '.':
        numValid = traverse(record[1:], sizes)
    elif record[0] == '#':
        if len(record) >= sizes[0] and '.' not in record[:sizes[0]] and (len(record) == sizes[0] or record[sizes[0]] != '#'):
            numValid = traverse(record[sizes[0]+1:],sizes[1:])
        else:
            numValid = 0
    elif record[0] == '?':
        numValid = traverse('.' + record[1:], sizes) + traverse('#' + record[1:], sizes)
    cache[(record, sizes)] = numValid
    return numValid
#######################

def part1(input):
    print("Part 1: ")
    sum = 0
    for line in input:
        [record, sizes] = line.split()
        sizes = tuple([int(x) for x in sizes.split(',')])
        # print(record)
        # print(sizes)

        # num = dfs(record, sizes, 0, '')
        num = traverse(record, sizes)

        sum += num
    print(sum)
        

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for line in input:
        [record, sizes] = line.split()
        sizes = [int(x) for x in sizes.split(',')]
        unfoldedRecord = record
        for i in range(4):
            unfoldedRecord += '?' + record
        unfoldedSizes = tuple([size for i in range(5) for size in sizes])
        # print(unfoldedRecord)
        # print(unfoldedSizes)
        sum += traverse(unfoldedRecord, unfoldedSizes)
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)


timeFunction(part1, input)
timeFunction(part2, input)
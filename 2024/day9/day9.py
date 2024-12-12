import sys
import os
import collections
import copy
import functools
import re
import itertools
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        return f.readline()

def decompress(input):
    space = False
    output = []
    id = 0
    for digit in input:
        output.extend([('.' if space else str(id)) for i in range(int(digit))])
        space = not space
        id += 1 if space else 0
    return output

def iterateReversedIdx(input, i):
    i -= 1
    while input[i] == '.':
        i -= 1
    return i

def compact(input):
    reversedIdx = iterateReversedIdx(input, len(input))
    output = []
    for i, c in enumerate(input):
        if c != '.':
            output.append(c)
        else:
            if i >= reversedIdx:
                return output[:reversedIdx+1]
            output.append(input[reversedIdx])
            reversedIdx = iterateReversedIdx(input, reversedIdx)

def checksum(input):
    return sum(i * int(c if c != '.' else 0) for i, c in enumerate(input))

def part1(input):
    print("Part 1: ")
    decompressed = decompress(input)
    # prettyPrintMatrix([decompressed])
    compacted = compact(decompressed)
    # prettyPrintMatrix([compacted])
    print(checksum(compacted))

def getChunkFromEnd(input, tailIdx):
    c = input[tailIdx]
    end = tailIdx
    chunk = [c]
    tailIdx -= 1
    while c == input[tailIdx]:
        chunk.append(input[tailIdx])
        tailIdx -= 1
    start = end + 1 - len(chunk)
    # move tailIdx to end of next chunk (skip dots)
    while tailIdx > 0 and input[tailIdx] == '.':
        tailIdx -= 1
    return chunk, (start, end), tailIdx

def fillInEarliestLargeEnoughSpace(input, chunk, chunkIndices):
    i = 0
    spaceSize = 0
    while i < chunkIndices[0]:
        if input[i] == '.':
            spaceSize += 1
            if spaceSize == len(chunk):
                # move chunk
                for j in range(len(chunk)):
                    input[i - j] = chunk[0]
                for k in range(chunkIndices[0], chunkIndices[1] + 1):
                    input[k] = '.'
                return
        else: 
            spaceSize = 0
        i += 1

def compact2(input):
    tailIdx = len(input) - 1
    while tailIdx > 0:
        chunk, chunkIndices, tailIdx = getChunkFromEnd(input, tailIdx)
        # print("chunk: {}, chunkIndices: {}, tailIdx: {}".format(chunk, chunkIndices, tailIdx))
        fillInEarliestLargeEnoughSpace(input, chunk, chunkIndices)
        # prettyPrintMatrix([input])
    # print(input)

def part2(input):
    print("\nPart 2: ")
    input = decompress(input)
    # prettyPrintMatrix([input])
    compact2(input)
    print(checksum(input))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)
import os
import re
from collections import deque

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def part1(input):
    print("Part 1: ")
    sum = 0
    for line in input:
        cardScore = 0
        winners = set(re.findall("\d+", line.split("|")[0].split(":")[1]))
        myCard = re.findall("\d+", line.split("|")[1])
        for n in myCard:
            if n in winners:
                if cardScore == 0:
                    cardScore = 1
                else:
                    cardScore = cardScore * 2
        sum = sum + cardScore
    print(sum)

def part2(input):
    print("\nPart 2: ")
    sum = 0
    processQueue = deque(range(len(input)))
    # For a given index, we should only need to compute the winners once, and store in a dict.
    # Afterwards, when we pop a line from the queue that we've seen before, we should make dict lookup for what resulting line indices to put on process queue  
    resultCache = {}
    while processQueue:
        i = processQueue.popleft()
        if i in resultCache:
            for copy in resultCache[i]:
                processQueue.append(copy)
            sum = sum + 1
            continue
        else:
            line = input[i]
            winners = set(re.findall("\d+", line.split("|")[0].split(":")[1]))
            myCard = re.findall("\d+", line.split("|")[1])
            j = 1
            copies = []
            for n in myCard:
                if n in winners:
                    copies.append(i+j)
                    processQueue.append(i+j)
                    j = j + 1
            resultCache[i] = copies
            sum = sum + 1
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)
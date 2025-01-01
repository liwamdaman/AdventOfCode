import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [int(line.rstrip()) for line in lines]

def generateNextSecret(secret):
    curr = secret
    curr = ((curr * 64) ^ curr) % 16777216
    curr = ((curr // 32) ^ curr) % 16777216
    curr = ((curr * 2048) ^ curr) % 16777216
    return curr

def part1(input):
    print("Part 1: ")
    sum = 0
    for initialSecret in input:
        secret = initialSecret
        for i in range(2000):
            secret = generateNextSecret(secret)
        # print(secret)
        sum += secret
    print(sum)

def part2(input):
    print("\nPart 2: ")
    priceSequencesToBananas = {}
    for initialSecret in input:
        secret = initialSecret
        prevPrice = initialSecret % 10
        priceSequence = []
        sequencesSeen = set()
        for i in range(2000):
            secret = generateNextSecret(secret)
            price = secret % 10
            priceChange = price - prevPrice
            priceSequence.append(priceChange)
            prevPrice = price
            if len(priceSequence) >= 4:
                seq = (priceSequence[-4], priceSequence[-3], priceSequence[-2], priceSequence[-1])
                # only count the bananas for the first time the sequence is seen for a givin buyer
                if seq not in sequencesSeen:
                    priceSequencesToBananas[seq] = priceSequencesToBananas.get(seq, 0) + price
                sequencesSeen.add(seq)
    maxBananas = 0
    bestSequence = ()
    for sequences, bananas in priceSequencesToBananas.items():
        if bananas > maxBananas:
            maxBananas = bananas
            bestSequence = sequences
    print(bestSequence)
    print(maxBananas)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)
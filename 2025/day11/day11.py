import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
import math
sys.setrecursionlimit(10000)
sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def parseEdges(lines):
    edges = collections.defaultdict(list)
    for line in lines:
        input, outs = line.split(': ')
        outs = outs.split(' ')
        for out in outs:
            edges[input].append(out)
    # print(edges)
    return edges

def part1(input):
    print("Part 1: ")
    edges = parseEdges(input)
    def dfs(node, cache):
        if node == 'out':
            return 1
        if node in cache:
            return cache[node]
        res = 0
        for out in edges[node]:
            res += dfs(out, cache)
        cache[node] = res
        return cache[node]
    res = dfs('you', {})
    print(res)

def part2(input):
    print("\nPart 2: ")
    edges = parseEdges(input)

    def dfs(node, cache, dacVisited, fftVisited):
        if node == 'out':
            return 1 if dacVisited and fftVisited else 0

        # Key the cache by the state tuple
        cache_key = (node, dacVisited, fftVisited)
        if cache_key in cache:
            return cache[cache_key]

        dac = dacVisited
        fft = fftVisited
        if node == 'dac':
            dac = True
        if node == 'fft':
            fft = True

        res = 0
        for out in edges[node]:
            res += dfs(out, cache, dac, fft)

        cache[cache_key] = res
        return cache[cache_key]
    res = dfs('svr', {}, False, False)
    print(res)

dirname = os.path.dirname(__file__)
filename1 = os.path.join(dirname, 'input.txt')
input1 = parseInput(filename1)
filename2 = os.path.join(dirname, 'input.txt')
input2 = parseInput(filename2)

part1(input1)
part2(input2)
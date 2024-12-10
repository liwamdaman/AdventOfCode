import sys
import os
import collections
import functools
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseRules(rules):
    # each value contains the list of pages that come after the keyed page
    orders = {}
    for rule in rules.split():
        [before, after] = rule.split('|')
        orders.setdefault(before, set()).add(after)
    return orders

def parseUpdates(updates):
    return [line.rstrip().split(',') for line in updates.split()]

def parseInput(filename):
    with open(filename) as f:
        [rules, updates] = f.read().split('\n\n')
        rules = parseRules(rules)
        updates = parseUpdates(updates)
        # print(rules)
        # print(updates)
        return rules, updates

def part1(rules, updates):
    print("Part 1: ")
    sum = 0
    for update in updates:
        broken = False
        previousPages = []
        for page in update:
            for prev in previousPages:
                if page in rules and prev in rules[page]:
                    # rule is broken
                    broken = True
            previousPages.append(page)
        if broken == False:
            sum = sum + int(update[len(update)//2])
    print(sum)

def getMiddle(rules, update):
    previousPages = []
    for page in update:
        for prev in previousPages:
            if page in rules and prev in rules[page]:
                # rule is broken, apply sort and get middle
                def compare(first, second):
                    if first in rules and second in rules[first]:
                        return -1
                    if second in rules and first in rules[second]:
                        return 1
                    return 0
                updateSorted = sorted(update, key=functools.cmp_to_key(compare))
                # print(updateSorted)
                return int(updateSorted[len(updateSorted)//2])
        previousPages.append(page)
    return 0

def part2(rules, updates):
    print("\nPart 2: ")
    sum = 0
    for update in updates:
        sum = sum + getMiddle(rules, update)
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
rules, updates = parseInput(filename)

part1(rules, updates)
part2(rules, updates)
import os
import re

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines
    
maximums = {"red": 12, "green": 13, "blue": 14}

def isSetPossible(set):
    # print(set)
    blue = re.search("(\d+) blue", set)
    numBlue = 0 if blue == None else int(blue.group(1))
    red = re.search("(\d+) red", set)
    numRed = 0 if red == None else int(red.group(1))
    green = re.search("(\d+) green", set)
    numGreen = 0 if green == None else int(green.group(1))
    return numBlue <= maximums["blue"] and numRed <= maximums["red"] and numGreen <= maximums["green"]

def part1(input):
    print("Part 1: ")
    sum = 0
    for i, line, in enumerate(input):
        isGamePossible = True
        game = line.split(":")[1]
        # print(game)
        for set in game.split(";"):
            isGamePossible = isGamePossible and isSetPossible(set)
        if isGamePossible:
            sum = sum + i + 1
    print(sum)

def processSet(set, mins):
    blue = re.search("(\d+) blue", set)
    numBlue = 0 if blue == None else int(blue.group(1))
    mins["blue"] = max(mins["blue"], numBlue)
    red = re.search("(\d+) red", set)
    numRed = 0 if red == None else int(red.group(1))
    mins["red"] = max(mins["red"], numRed)
    green = re.search("(\d+) green", set)
    numGreen = 0 if green == None else int(green.group(1))
    mins["green"] = max(mins["green"], numGreen)

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for line in input:
        mins = {"red": 0, "green": 0, "blue": 0}
        game = line.split(":")[1]
        for set in game.split(";"):
            processSet(set, mins)
        # print(mins)
        sum = sum + (mins["blue"] * mins["red"] * mins["green"])
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)
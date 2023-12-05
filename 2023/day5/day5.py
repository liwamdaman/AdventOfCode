import os
import sys

seeds = []
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

def parseLineToMapping(line, mapping):
    mapping.append(tuple([int(n) for n in line.split()]))

def parseInput(filename):
    with open(filename) as f:
        seeds.extend([int(seed) for seed in f.readline().split(": ")[1].split()])
        f.readline()
        f.readline()
        while (line := f.readline()) != "\n":
            parseLineToMapping(line, seedToSoil)
        f.readline()
        while (line := f.readline()) != "\n":
            parseLineToMapping(line, soilToFertilizer)
        f.readline()
        while (line := f.readline()) != "\n":
            parseLineToMapping(line, fertilizerToWater)
        f.readline()
        while (line := f.readline()) != "\n":
            parseLineToMapping(line, waterToLight)
        f.readline()
        while (line := f.readline()) != "\n":
            parseLineToMapping(line, lightToTemperature)
        f.readline()
        while (line := f.readline()) != "\n":
            parseLineToMapping(line, temperatureToHumidity)
        f.readline()
        while line := f.readline():
            parseLineToMapping(line, humidityToLocation)

####### PART 1 #######

def getMapping(val, mappings):
    for mapping in mappings:
        (dest, source, range) = mapping
        if source <= val < source+range:
            return dest + (val-source)
    return val

def part1(input):
    print("Part 1: ")
    lowest = sys.maxsize
    for seed in seeds:
        val = getMapping(seed, seedToSoil)
        val = getMapping(val, soilToFertilizer)
        val = getMapping(val, fertilizerToWater)
        val = getMapping(val, waterToLight)
        val = getMapping(val, lightToTemperature)
        val = getMapping(val, temperatureToHumidity)
        location = getMapping(val, humidityToLocation)
        if location < lowest:
            lowest = location
    print(lowest)

####### PART 2 #######

def part2BruteForce():
    print("\nPart 2: ")
    lowest = sys.maxsize
    actualSeeds = []
    for i in range(0, len(seeds), 2):
        actualSeeds.append((seeds[i], seeds[i] + seeds[i+1]))
    for seedRange in actualSeeds:
        for seed in range(seedRange[0], seedRange[1]):
            val = getMapping(seed, seedToSoil)
            val = getMapping(val, soilToFertilizer)
            val = getMapping(val, fertilizerToWater)
            val = getMapping(val, waterToLight)
            val = getMapping(val, lightToTemperature)
            val = getMapping(val, temperatureToHumidity)
            location = getMapping(val, humidityToLocation)
            if location < lowest:
                lowest = location
    print(lowest)

####### PART 2 IMPROVED #######

def getMappingReversed(val, mappings):
    for mapping in mappings:
        (source, dest, range) = mapping
        if source <= val < source+range:
            return dest + (val-source)
    return val

def part2BruteForceInverted():
    print("\nPart 2: ")
    actualSeeds = []
    for i in range(0, len(seeds), 2):
        actualSeeds.append((seeds[i], seeds[i] + seeds[i+1]))

    location = 0
    while True:
        val = getMappingReversed(location, humidityToLocation)
        val = getMappingReversed(val, temperatureToHumidity)
        val = getMappingReversed(val, lightToTemperature)
        val = getMappingReversed(val, waterToLight)
        val = getMappingReversed(val, fertilizerToWater)
        val = getMappingReversed(val, soilToFertilizer)
        seed = getMappingReversed(val, seedToSoil)
        for seedRange in actualSeeds:
            if seedRange[0] <= seed < seedRange[1]:
                print((seed, location))
                return
        location += 1

####### PART 2 EFFICIENT #######

def getIntervalOverlap(interval1, interval2):
    overlap = (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))
    if overlap[0] > overlap[1]:
        return None
    return overlap

def removeOverlapFromInterval(interval, overlap):
    resultingSplitIntervals = []
    # an overlapping interval while be a subset of the interval
    if overlap[0] > interval[0]:
        resultingSplitIntervals.append((interval[0], overlap[0]))
    if overlap[1] < interval[1]:
        resultingSplitIntervals.append((overlap[1], interval[1]))
    return resultingSplitIntervals

def getSourceIntervalFromMapping(mapping):
    (dest, source, range) = mapping
    return (source, source+range)

def getMappedInterval(interval, mapping):
    (dest, source, range) = mapping
    return (interval[0] + dest-source, interval[1] + dest-source)

def applyMappingsToIntervals(intervals, mappings):
    resultingMappedIntervals = []
    for interval in intervals:
        resultingMappedIntervals.extend(applyMappingsToInterval(interval, mappings))
    return resultingMappedIntervals

def applyMappingsToInterval(interval, mappings):
    subIntervals = [interval]
    resultingMappedIntervals = []
    for mapping in mappings:
        for subInterval in subIntervals:
            overlap = getIntervalOverlap(subInterval, getSourceIntervalFromMapping(mapping))
            if overlap:
                resultingMappedIntervals.append((getMappedInterval(overlap, mapping)))
                subIntervals.remove(subInterval)
                subIntervals.extend(removeOverlapFromInterval(subInterval, overlap))
                break
    # map remaining subintervals to themselves
    resultingMappedIntervals.extend(subIntervals)
    return resultingMappedIntervals

def part2IntervalSplitting():
    print("\nPart 2: ")
    actualSeeds = []
    for i in range(0, len(seeds), 2):
        actualSeeds.append((seeds[i], seeds[i] + seeds[i+1]))
    resultingMappedIntervals = applyMappingsToIntervals(actualSeeds, seedToSoil)
    resultingMappedIntervals = applyMappingsToIntervals(resultingMappedIntervals, soilToFertilizer)
    resultingMappedIntervals = applyMappingsToIntervals(resultingMappedIntervals, fertilizerToWater)
    resultingMappedIntervals = applyMappingsToIntervals(resultingMappedIntervals, waterToLight)
    resultingMappedIntervals = applyMappingsToIntervals(resultingMappedIntervals, lightToTemperature)
    resultingMappedIntervals = applyMappingsToIntervals(resultingMappedIntervals, temperatureToHumidity)
    locations = applyMappingsToIntervals(resultingMappedIntervals, humidityToLocation)
    # print(locations)
    lowestLocation = min([location[0] for location in locations])
    print(lowestLocation)

##########################

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
# part2BruteForce()
# part2BruteForceInverted()
part2IntervalSplitting()
with open('input.txt') as f:
    lines = f.readlines()

numOverlap=0

for line in lines:
    first, second = line.split(',')
    firstStart, firstEnd = map(int, first.split('-'))
    secondStart, secondEnd = map(int, second.split('-'))
    # https://www.baeldung.com/cs/finding-all-overlapping-intervals
    if not max(firstStart, secondStart) > min(firstEnd, secondEnd):
        numOverlap += 1

print(numOverlap)
def priority(c):
    if ord(c) >= 97:
        # lower case
        return ord(c) - 96
    else:
        # upper case
        return ord(c) - 38

with open('input.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    firstHalf = line[:len(line)//2]
    secondHalf = line[len(line)//2:]
    # print(firstHalf)
    # print(secondHalf)
    s = set()
    for c in firstHalf:
        s.add(c)
    for c in secondHalf:
        if c in s:
            total += priority(c)
            # print(c)
            break

print(total)

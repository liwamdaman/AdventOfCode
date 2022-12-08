PointMapping = {
    'X':1, 'Y':2, 'Z':3
}

with open('input.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    opp, mine = line.split()
    score += PointMapping[mine]
    result = (ord(mine)-88 - (ord(opp)-65)) % 3
    # print("{}, {}, {}".format(opp, mine, result))
    match result:
        case 0:
            score += 3
        case 1:
            score += 6
        case 2:
            score += 0

print(score)
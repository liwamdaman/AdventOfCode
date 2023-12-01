PointMapping = {
    'rock':1, 'paper':2, 'scissors':3
}

# I'm too lazy to think
MatchupMapping = {
    'A': {
        'X': 0 + PointMapping['scissors'],
        'Y': 3 + PointMapping['rock'],
        'Z': 6 + PointMapping['paper']
    },
    'B': {
        'X': 0 + PointMapping['rock'],
        'Y': 3 + PointMapping['paper'],
        'Z': 6 + PointMapping['scissors']
    },
    'C': {
        'X': 0 + PointMapping['paper'],
        'Y': 3 + PointMapping['scissors'],
        'Z': 6 + PointMapping['rock']
    }
}

with open('input.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    opp, mine = line.split()
    score += MatchupMapping[opp][mine]

print(score)

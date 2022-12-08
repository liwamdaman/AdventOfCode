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

i = 1
temp = []
for line in lines:
    if i == 3:
        temp.append(line.strip())
        # print(temp)
        i = 1

        # s1 = set()
        # for c in temp[0]:
        #     s1.add(c)
        # s2 = set()
        # for c in temp[1]:
        #     if c in s1:
        #         s2.add(c)
        # for c in temp[2]:
        #     if c in s2:
        #         # print(c)
        #         total += priority(c)
        #         break

        ## More Understandable ##
        s1 = set()
        for c in temp[0]:
            s1.add(c)
        s2 = set()
        for c in temp[1]:
            s2.add(c)
        s3 = set()
        for c in temp[2]:
            s3.add(c)
        intersection = s1.intersection(s2, s3)
        total += priority(intersection.pop())

        temp = []
    else:
        temp.append(line.strip())
        i += 1

print(total)
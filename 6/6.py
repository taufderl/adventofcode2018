from collections import defaultdict
import operator

with open('input.txt') as infile:
    data = infile.readlines()

def manhattan(c1, c2):
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])

coords = []
for i, line in enumerate(data):
    x, y = line.strip().split(',')
    x, y = int(x), int(y)
    coords.append((x,y))

maxx = max([x for x,y in coords])
maxy = max([y for x,y in coords])

counts = defaultdict(int)
regionsize = 0 # part 2
for i in range(maxx+2):
    for j in range(maxy+2):
        dist, index = None,None
        dsum = 0 #part 2
        for _id, c in enumerate(coords):
            m = manhattan((i,j), c)
            if dist == None or m < dist:
                dist, index = m, _id
            elif m == dist: # same distance here
                dist, index = m, '.'
            dsum += m # part2
        if i in (0, maxx+1) or j in (0, maxy+1):
            counts[index] = -99999999 #infinite!
        counts[index] += 1
        if dsum < 10000: #part 2
            regionsize += 1

p, s = max(counts.items(), key=operator.itemgetter(1))
print('The region around point {p} has the biggest size: {s}.'.format(p=p,s=s))
print('The region has the size {s}.'.format(s=regionsize))

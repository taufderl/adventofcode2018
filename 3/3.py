from collections import defaultdict

with open('input.txt') as infile:
  data = infile.readlines()

field = defaultdict(lambda: defaultdict(int))

for line in data:
    _, _, coords, size = line.split(' ')
    x, y = coords[:-1].split(',')
    xlen, ylen = size.split('x')
    x, y = int(x), int(y)
    xlen, ylen = int(xlen), int(ylen)

    for i in range(x, x+xlen):
        for j in range(y, y+ylen):
            field[i][j] += 1

count = 0
for i in field.keys():
    for j in field[i].keys():
        if field[i][j] > 1:
            count += 1
print('Fiels with more than 1 claim:', count)

# part 2
field = defaultdict(lambda: defaultdict(int))
ids_overlapping = set()
ids_all = set()
for line in data:
    _id, _, coords, size = line.split(' ')
    _id = int(_id[1:])
    ids_all.add(_id)
    x, y = coords[:-1].split(',')
    xlen, ylen = size.split('x')
    x, y = int(x), int(y)
    xlen, ylen = int(xlen), int(ylen)

    for i in range(x, x+xlen):
        for j in range(y, y+ylen):
            if not field[i][j]:
                field[i][j] = _id
            else:
                ids_overlapping.add(field[i][j])
                ids_overlapping.add(_id)
result = ids_all.difference(ids_overlapping)
print('Field without overlapping claims:', result)


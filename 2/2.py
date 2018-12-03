from collections import defaultdict

with open('input.txt') as infile:
    data = infile.readlines()

doubles = 0
triples = 0
for line in data:
    freqs = defaultdict(int)
    for letter in line:
        freqs[letter] += 1
    if 2 in freqs.values():
        doubles += 1
    if 3 in freqs.values():
        triples += 1

print('Doubles: ', doubles)
print('Triples: ', triples)
print('Checksum:', doubles*triples)

def recursive_levenshtein(string_1, string_2, len_1=None, len_2=None, offset_1=0, offset_2=0, memo=None):
    if len_1 is None:
        len_1 = len(string_1)

    if len_2 is None:
        len_2 = len(string_2)

    if memo is None:
        memo = {}

    key = ','.join([str(offset_1), str(len_1), str(offset_2), str(len_2)])

    if memo.get(key) is not None:
        return memo[key]

    if len_1 == 0:
        return len_2
    elif len_2 == 0:
        return len_1

    cost = 0

    if string_1[offset_1] != string_2[offset_2]:
        cost = 1

    dist = min(
        recursive_levenshtein(string_1, string_2, len_1 - 1, len_2, offset_1 + 1, offset_2, memo) + 1,
        recursive_levenshtein(string_1, string_2, len_1, len_2 - 1, offset_1, offset_2 + 1, memo) + 1,
        recursive_levenshtein(string_1, string_2, len_1 - 1, len_2 - 1, offset_1 + 1, offset_2 + 1, memo) + cost,
    )
    memo[key] = dist
    return dist

print("Find close strings")
for line in data:
    for line2 in data:
        l = recursive_levenshtein(line, line2)
        if l == 1:
            print(line, line2)

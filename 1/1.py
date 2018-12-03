import os


with open('input.txt') as infile:
  data = infile.readlines()

freq = 0
for line in data:
    if '+' in line:
        line = line[1:]
    i = int(line)
    freq += i

print('Final freq: ', freq)

freq = 0
freqs = set([0])
first_twice = None
while first_twice == None:
    for line in data:
        if '+' in line:
            line = line[1:]
        i = int(line)
        freq += i
        if first_twice == None and freq in freqs:
            first_twice = freq
            break
        freqs.add(freq)

print('First twice: ', first_twice)

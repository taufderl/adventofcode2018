from collections import defaultdict

with open('input.txt') as infile:
  data = infile.readlines()

data = sorted(data)

cur_guard = 0
fell_asleep = None
guards = defaultdict(lambda: defaultdict(int))
for line in data:
    _date, _action = line.split(']')
    minute = int(_date[-2:])
    if '#' in _action:
        cur_guard = int(_action.split(' ')[2][1:])
    elif 'sleep' in _action:
        fell_asleep = minute
    elif 'wake' in _action:
        for i in range(fell_asleep, minute):
            guards[cur_guard][i] += 1

guard, score = 0, 0
for g in guards.keys():
    total_sleep = sum(guards[g].values())
    if total_sleep > score:
        guard, score = g, total_sleep
minute, score = 0, 0
for m in guards[guard].keys():
    if guards[guard][m] > score:
        minute, score = m, guards[guard][m]

print('Stragegy 1: Guard #{g} sleeps the most ({s}). He is most asleep in minute {m}, solution: {a}.'.format(g=guard, m=minute, s=score, a=minute*guard))

minute, guard, score = 0, 0, 0
for g in guards.keys():
    for m in guards[g].keys():
        if guards[g][m] > score:
            guard, minute, score = g, m, guards[g][m]

print('Stragegy 2: Guard #{g} is the most asleep ({s}) within the same minute ({m}), solution: {a}.'.format(g=guard, m=minute, s=score, a=minute*guard))




with open('input.txt') as infile:
    data = infile.readlines()

def react(pol):
    i = 0
    while i < len(pol)-1:
        if abs(ord(pol[i]) - ord(pol[i+1])) == 32:
            del pol[i:i+2]
            if i>0:
                i -= 1
        else:
            i += 1
    return len(pol)

for line in data:
    pol = list(line.strip())
    l = react(pol)
    print('The length of the fully reacted base polymer is {l}'.format(l=l))

# part 2
for line in data:
    base_pol = list(line.strip())
    smallest = None
    for letter in range(65,91):
        pol = [l for l in base_pol if (ord(l) != letter and ord(l) != letter+32)]
        react_len = react(pol)
        print("Polymer length without letters {letters}: {l}".format(letters=chr(letter)+chr(letter+32), l=react_len))
        if smallest is None or smallest > react_len:
            smallest = react_len
    print('The length of the shortest polymer is {l}'.format(l=smallest))

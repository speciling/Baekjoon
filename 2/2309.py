from itertools import combinations

dwarfs = [0]*9
for i in range(9):
    dwarfs[i] = int(input())
dwarfs.sort()

for c in combinations(dwarfs, 7):
    if sum(c) == 100:
        for h in c:
            print(h)
        break
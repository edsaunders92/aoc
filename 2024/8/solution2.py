import sys
import itertools
from collections import defaultdict


graph = list(map(str.rstrip, sys.stdin))
antennas = defaultdict(list)

for r,row in enumerate(graph):
    for c,val in enumerate(row):
        if val != '.':
            antennas[val].append((r,c))

count = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        if (graph[r][c] != '.'):
            count+=1
        else:
            is_antinode = False
            for freq,group in antennas.items():
                for (ar,ac),(br,bc) in itertools.combinations(group, 2):
                    if (bc - c)* (ar - r) == (br - r) * (ac - c):
                        is_antinode = True
            if is_antinode:
                count += 1
print(count)







import sys
import itertools
from collections import defaultdict


graph = list(map(str.rstrip, sys.stdin))
antennas = defaultdict(list)

for r,row in enumerate(graph):
    for c,val in enumerate(row):
        if val != '.':
            antennas[val].append((r,c))

antinodes = set()
for frequency,locations in antennas.items():
    for (ax,ay),(bx,by) in itertools.combinations(locations,2):
         antinodes.add((-bx + 2 * ax,-by + 2 * ay))
         antinodes.add((-ax + 2 * bx,-ay + 2 * by))

count = 0
for x,y in antinodes:
    if x >= 0 and y >= 0 and x < len(graph) and y < len(graph[0]):
        count+=1
print(count)



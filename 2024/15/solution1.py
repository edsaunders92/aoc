import sys
import re

directions = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
}

inp = list(map(str.rstrip, sys.stdin))
pivot = inp.index("")
graph = [[a for a in line] for line in inp[:pivot]]
moves = "".join(inp[1+pivot:])

position = None

def iterator(graph):
    for r,row in enumerate(graph):
        for c,val in enumerate(row):
            yield (val,r,c)


# find start
for val,r,c in iterator(graph):
    if val == '@':
        position = (r,c)

print("inital state")
print("\n".join(["".join(line) for line in graph]))
print("")
for move in moves:
    direction = directions[move]
    r,c = position
    while graph[r][c] != '.' and graph[r][c] != '#':
        r += direction[0]
        c += direction[1]
    if graph[r][c] == '.':
        graph[r][c] = 'O'
        graph[position[0]][position[1]] = '.'
        position = (position[0] + direction[0], position[1] + direction[1])
        graph[position[0]][position[1]] = '@'
    print("move",move)
    print("\n".join(["".join(line) for line in graph]))
    print("")

# calculate score
def score(val,r,c):
    if (val != 'O'):
        return 0
    return r * 100 + c

print(sum([score(*a) for a in iterator(graph)]))

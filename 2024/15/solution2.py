import sys

directions = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
}

def mapping(s):
    return {
        '#': '##',
        'O': '[]',
        '@': '@.',
        '.': '..',
    }[s];

inp = list(map(str.rstrip, sys.stdin))
pivot = inp.index("")

graph = [list("".join(list(map(mapping, line)))) for line in inp[:pivot]]

print(graph)

moves = "".join(inp[1+pivot:])

position = None

def iterator(graph):
    for r,row in enumerate(graph):
        for c,val in enumerate(row):
            print(val,r,c)
            yield (val,r,c)


# find start
for val,r,c in iterator(graph):
    if val == '@':
        position = (r,c)

print(position)

print("inital state")
print("\n".join(["".join(line) for line in graph]))
print("")
for move in moves:
    direction = directions[move]
    r,c = position
    prev = '@'
    while graph[r][c] != '.' and graph[r][c] != '#' and (move == '>' or move == '<' or prev == '@' or graph[r][c] == prev):
        prev = graph[r][c]
        r += direction[0]
        c += direction[1]
    if graph[r][c] == '.' and (move == '<' or move == '>' or prev == '@' or (prev == '[' and c < len(graph[r]) and graph[r][c + 1] == '.') or  (prev == ']' and c < len(graph[r]) and graph[r][c - 1] == '.')):
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

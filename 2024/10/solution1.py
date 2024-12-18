import sys


graph = [[int(i) for i in s] for s in map(str.rstrip, sys.stdin)]


def score(a,b):
    if graph[a][b] != 0:
        return 0
    step = set()
    step.add((a,b))
    nxt = set()

    for n in range(1,10):
        for node in step:
            for d in [(1,0),(-1,0),(0,-1),(0,1)]:
                newnode = (node[0] + d[0], node[1] + d[1])
                if newnode[0] >= 0 and newnode[1] >= 0 and newnode[0] < len(graph) and newnode[1] < len(graph[0]) and graph[newnode[0]][newnode[1]] == n:
                    nxt.add(newnode)
        step = nxt
        nxt = set()

    return len(step)

t = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        t += score(r,c)
print(t)


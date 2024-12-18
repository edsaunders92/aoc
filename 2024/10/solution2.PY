import sys


graph = [[int(i) for i in s] for s in map(str.rstrip, sys.stdin)]
score = [[1 if i == 9 else 0 for i in line] for line in graph]

total = 0
for i in range(8,-1,-1):
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            if graph[r][c] == i:
                for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newnode = (r + d[0], c + d[1])
                    if newnode[0] >= 0 and newnode[1] >= 0 and newnode[0] < len(graph) and newnode[1] < len(graph[0]) and graph[newnode[0]][newnode[1]] == i + 1:
                        score[r][c] += score[newnode[0]][newnode[1]] 
                if i == 0:
                    total += score[r][c]

print(total)

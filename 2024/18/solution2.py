import sys
import re

n = 71
grid = [[True for _ in range(n)] for _ in range (n)]

def dijkstra(graph): 
    dist = {}
    queue = set()

    for i in range(n):
        for j in range(n):
            if (graph[i][j]):
                dist[(i,j)] = float('inf')
                queue.add((i,j))

    dist[(0,0)] = 0

    while len(queue) > 0:
        x,y = min(queue, key=lambda x:dist[x])
        queue.remove((x,y))

        for nei in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nei in queue:
                dist[nei] = min(dist[nei], dist[(x,y)] + 1)

    return dist[(n-1,n-1)]

count = 0
for line in sys.stdin:
    line = line.rstrip()
    x,y = line.split(',')
    x,y = int(x),int(y)
    grid[y][x] = False
    count+=1
    if (count < 2957):
        continue
    d = dijkstra(grid)
    print(count,d)
    print(line)
    break



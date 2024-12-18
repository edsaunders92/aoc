import sys
import itertools

graph = [[a for a in line] for line in map(str.rstrip, sys.stdin)]

price = 0 
for r,c in itertools.product(range(len(graph)), range(len(graph[0]))):
    if graph[r][c] != '.':
        region = set()
        region.add((r,c))
        stack = [(r,c)]
        perimeter = 0
        while len(stack):
            cr,cc = stack.pop()
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = cr + dr, cc + dc
                if (nr < 0 or nc < 0 or nr >= len(graph) or nc >= len(graph[0]) or graph[nr][nc] != graph[cr][cc]):
                    perimeter += 1
                else:
                    if (nr,nc) not in region:
                        stack.append((nr,nc))
                        region.add((nr,nc))
        price += perimeter * len(region)
        for cr,cc in region:
            graph[cr][cc] = '.'

print(price)


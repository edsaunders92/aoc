import sys
import itertools
from collections import defaultdict

graph = [[a for a in line] for line in map(str.rstrip, sys.stdin)]

price = 0 


def debug(region):
    minr = min([r for (r,_) in region])
    minc = min([c for (_,c) in region])
    maxr = max([r for (r,_) in region])
    maxc = max([c for (_,c) in region])
    graph = [["." for c in range(1 + maxc - minc)] for r in range(1 + maxr - minr)]
    for (r,c) in region:
        graph[r - minr][c - minc] = 'X'
    for line in graph:
        print("".join(line))



for r,c in itertools.product(range(len(graph)), range(len(graph[0]))):
    if graph[r][c] != '.':
        region = set()
        region.add((r,c))
        stack = [(r,c)]
        while len(stack):
            cr,cc = stack.pop()
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = cr + dr, cc + dc
                if not (nr < 0 or nc < 0 or nr >= len(graph) or nc >= len(graph[0]) or graph[nr][nc] != graph[cr][cc]):
                    if (nr,nc) not in region:
                        stack.append((nr,nc))
                        region.add((nr,nc))
        print(graph[r][c])
        debug(region)
        for cr,cc in region:
            graph[cr][cc] = '.'
        area = len(region)
        sides = defaultdict(int)

        for cr,cc in region:
            sides[((cr,cc),(0,1))] += 1
            sides[((cr,cc),(1,0))] += 1
            sides[((cr,cc+1),(1,0))] += 1
            sides[((cr+1,cc),(0,1))] += 1

        sides = [side for (side,qty) in sides.items() if qty == 1]

        edges = 0
        while len(sides) != 0:
            edges += 1
            ((sr,sc),(dr,dc)) = sides.pop()
            # print((sr,sc),(dr,dc)) 
            cr = sr
            cc = sc
            while ((cr + dr, cc + dc),(dr,dc)) in sides:
                cr += dr
                cc += dc
                sides.remove(((cr,cc),(dr,dc)))
            cr = sr
            cc = sc
            while ((cr - dr, cc - dc),(dr,dc)) in sides:
                cr -= dr
                cc -= dc
                sides.remove(((cr,cc),(dr,dc)))

        print(edges,area, edges * area)
        price += edges * area

print(price)


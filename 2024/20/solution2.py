import sys

def parseinput():
    grid = []
    for line in sys.stdin:
        line = line.rstrip()
        line = list(line)
        grid.append(line)
    return grid

def iterate(grid, center = (0,0), d = 1000000):
    sr = max(0, center[0] - d)
    er = min(len(grid), center[0] + d + 1)
    sc = max(0, center[1] - d)
    ec = min(len(grid[0]), center[1] + d + 1)

    for r in range(sr,er):
        for c in range(sc,ec):
            yield (r,c),grid[r][c]


def find(grid, s):
    for coords,value in iterate(grid):
        if value == s:
            return coords

def dijkstra(grid, source):
    dist = {}
    queue = set()
    for coords,value in iterate(grid):
        if (value == '.' or value == 'E' or value == 'S'):
            dist[coords] = float('inf')
            queue.add(coords)
    dist[source] = 0

    while len(queue) > 0:
        c = min(queue, key=lambda x:dist[x])
        queue.remove(c)

        for nei in [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]:
            if nei in queue:
                dist[nei] = min(dist[nei], dist[c] + 1)

    return dist

def main(cheat):
    grid = parseinput()
    source = find(grid, 'S')
    goal = find(grid, 'E')
    fromstart = dijkstra(grid,source)
    fromgoal = dijkstra(grid,goal)
    target = fromstart[goal] - 100
    score = 0

    for c1,_ in iterate(grid):
        if c1 not in fromstart:
            continue
        if (fromstart[c1] >= target):
            continue
        for c2,_ in iterate(grid, c1, cheat):
            if c2 not in fromgoal:
                continue
            md = abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])
            d = fromstart[c1] + fromgoal[c2] + md
            if md <= cheat and d <= target:
                print(c1,c2)
                score += 1
    print(score)


if __name__ == '__main__':
    main(20)



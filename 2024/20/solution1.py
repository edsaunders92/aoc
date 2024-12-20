import sys

def parseinput():
    grid = []
    for line in sys.stdin:
        line = line.rstrip()
        line = list(line)
        grid.append(line)
    return grid

def iterate(grid):
    for row,r in enumerate(grid):
        for col,value in enumerate(r):
            yield ((row,col), value)


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

def main():
    grid = parseinput()
    source = find(grid, 'S')
    goal = find(grid, 'E')
    fromstart = dijkstra(grid,source)
    fromgoal = dijkstra(grid,goal)
    best = fromstart[goal]
    score = 0
    for c,value in iterate(grid):
        mins = float('inf')
        mine = float('inf')
        for nei in [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]:
            if nei in fromstart:
                mins = min(mins, fromstart[nei])
                mine = min(mine, fromgoal[nei])
        if best - mins - mine - 2 >= 100:
            score += 1

    print(score)


if __name__ == '__main__':
    main()


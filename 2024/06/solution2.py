import sys

dirs = [[1,0], [0, -1], [-1, 0], [0,1]]
dirsigns = "v<^>"
currentdir = None
position = (None,None)

graph = [[ i for i in l] for l in map(str.rstrip, sys.stdin)]

for r,row in enumerate(graph):
    for c,val in enumerate(row):
        for i,sign in enumerate(dirsigns):
            if sign == val:
                currentdir = i
                position = (r,c)

def isLoop():
    global graph

    pos = position
    cd = currentdir
    visited = set((position,cd))
    while True:
        new_position = (
            pos[0] + dirs[cd][0],
            pos[1] + dirs[cd][1],
        )
        if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(graph) or new_position[1] >= len(graph[0]):
            return False

        if graph[new_position[0]][new_position[1]] == '#':
            cd += 1
            cd %= len(dirs)
        elif (new_position,cd) in visited:
            return True
        else:
            pos = new_position
            visited.add((pos,cd))

count = 0

for r,row in enumerate(graph):
    for c,val in enumerate(row):
        print(r,c)
        if (r,c) == position:
            continue
        old = val
        graph[r][c] = '#'
        if isLoop():
            count += 1
        graph[r][c] = old

print(count)

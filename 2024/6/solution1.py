import sys

dirs = [[1,0], [0, -1], [-1, 0], [0,1]]
dirsigns = "v<^>"
currentdir = None
position = (None,None)

graph = list(map(str.rstrip, sys.stdin))

for r,row in enumerate(graph):
    for c,val in enumerate(row):
        for i,sign in enumerate(dirsigns):
            if sign == val:
                currentdir = i
                position = (r,c)

visited = set()

while True:
    new_position = (
        position[0] + dirs[currentdir][0],
        position[1] + dirs[currentdir][1],
    )
    if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(graph) or new_position[1] >= len(graph[0]):
        break 

    if graph[new_position[0]][new_position[1]] == '#':
        currentdir += 1
        currentdir %= len(dirs)
    else:
        visited.add(position)
        position = new_position
        visited.add(new_position)
                                        
print(len(visited))

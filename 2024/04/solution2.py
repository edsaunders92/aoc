import sys

search = list(map(str.rstrip, sys.stdin))

needle = "XMAS"

score = 0
for i in range(1,len(search) - 1):
    for j in range(1,len(search[0]) - 1):
        if search[i][j] == 'A' and (
            (search[i-1][j-1] == 'S' and search[i+1][j+1] == 'M') or
            (search[i-1][j-1] == 'M' and search[i+1][j+1] == 'S')
        ) and (
            (search[i-1][j+1] == 'S' and search[i+1][j-1] == 'M') or
            (search[i-1][j+1] == 'M' and search[i+1][j-1] == 'S')
        ):
            score += 1

print(score)

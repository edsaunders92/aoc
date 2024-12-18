import sys

search = list(map(str.rstrip, sys.stdin))

needle = "XMAS"

score = 0
for i in range(len(search)):
    for j in range(len(search[0])):
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if (di != 0 or dj != 0):
                    match = True
                    s = ""
                    for n in range(len(needle)):
                        ni = n * di + i
                        nj = n * dj + j
                        if ni < 0 or nj < 0 or ni >= len(search) or nj >= len(search[ni]) or search[ni][nj] != needle[n]:
                            match = False
                    if match:
                        score+=1

print(score)

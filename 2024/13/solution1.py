import sys
import re

def solve(ax,ay,bx,by,tx,ty):
    qa = 0
    best = float('inf')
    while (qa * ax <= tx):
        print(qa)
        qb = (tx - qa * ax) // bx
        if (qa * ax + qb * bx == tx and qa * ay + qb * by == ty):
            score = 3 * qa + qb
            if (score < best):
                best = score
        qa += 1
    if (best == float('inf')):
        return 0
    return best

re1 = "Button A: X\+(\d+), Y\+(\d+)"
re2 = "Button B: X\+(\d+), Y\+(\d+)"
re3 = "Prize: X=(\d+), Y=(\d+)"

total = 0
for line in map(str.rstrip, sys.stdin):
    match = re.match(re1, line)
    if match:
        ax = int(match.group(1))
        ay = int(match.group(2))

    match = re.match(re2, line)
    if match:
        bx = int(match.group(1))
        by = int(match.group(2))

    match = re.match(re3, line)
    if match:
        tx = int(match.group(1))
        ty = int(match.group(2))
        total += solve(ax,ay,bx,by,tx,ty)
print(total)

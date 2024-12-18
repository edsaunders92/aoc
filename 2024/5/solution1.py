import sys
from collections import defaultdict

blank_line_hit = False

rules = defaultdict(list)
updates = []
score = 0

def is_valid(update):
    hit = set()
    for page in update:
        for other in rules[page]:
            if other in hit:
                return False
        hit.add(page)
    return True

for line in map(str.rstrip, sys.stdin):
    if line == "":
        blank_line_hit = True
    elif blank_line_hit:
        update = ([int(i) for i in line.split(',')])
        if (is_valid(update)):
            score += update[len(update) // 2]
    else:
        a,b = [int(i) for i in line.split('|')]
        rules[a].append(b)

print(score)



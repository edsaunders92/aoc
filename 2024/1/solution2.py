import sys
from collections import defaultdict

list1 = []
list2 = defaultdict(int)
for a,b in [s.split() for s in map(str.rstrip, sys.stdin)]:
    list1.append(int(a))
    list2[int(b)] += 1

print(sum([a * list2[a] for a in list1]))

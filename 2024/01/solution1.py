import sys

list1 = []
list2 = []
for a,b in [s.split() for s in map(str.rstrip, sys.stdin)]:
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

print(sum([abs(a - b) for a,b in zip(list1, list2)]))

import sys


def parseline(line):
    parsed = line.split(': ')
    parsed[0] = int(parsed[0])
    parsed[1] = list(map(int, parsed[1].split()))
    return parsed

total = 0
for result, operators in map(parseline, map(str.rstrip, sys.stdin)):
    for i in range(2**(len(operators)-1)):
        s = operators[0]
        x = i
        for j in range(1, len(operators)):
            if (x % 2 == 0):
                s += operators[j]
            else:
                s *= operators[j]
            x //= 2
        if s == result:
            total += result
            break

print(total)

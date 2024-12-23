import sys


def parseline(line):
    parsed = line.split(': ')
    parsed[0] = int(parsed[0])
    parsed[1] = list(map(int, parsed[1].split()))
    return parsed

total = 0
for result, operators in map(parseline, map(str.rstrip, sys.stdin)):
    for i in range(3**(len(operators)-1)):
        s = operators[0]
        x = i
        for j in range(1, len(operators)):
            if (x % 3 == 0):
                s += operators[j]
            elif (x % 3 == 1):
                s *= operators[j]
            else:
                s = str(s)
                s += str(operators[j])
                s = int(s)
            x //= 3
        if s == result:
            total += result
            break

print(total)

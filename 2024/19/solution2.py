patterns = input().split(", ")

assert(input() == "")

memo = {"": 1}

def solve(line):
    if not line in memo:
        memo[line] = 0
        for pattern in patterns:
            if line.startswith(pattern):
                memo[line] += solve(line[len(pattern):])
    return memo[line]

s = 0
while True:
    try:
        line = input()
    except:
        break
    s += solve(line)
print(s)


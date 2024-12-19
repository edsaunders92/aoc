import sys
import re

patterns = input().split(", ")

assert(input() == "")

def solve(line):
    if line == "":
        return True

    for pattern in patterns:
        if line.startswith(pattern) and solve(line[len(pattern):]):
            return True
    return False

count = 0
while True:
    try:
        line = input()
    except:
        print(count)
        exit()
    if solve(line):
        count+=1


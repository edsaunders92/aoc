import re, sys

matches = re.finditer("mul\((\d{1,3}),(\d{1,3})\)", sys.stdin.read())

score = 0
for match in matches:
    score += int(match.group(1)) * int(match.group(2))
print(score)

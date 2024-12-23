import re, sys

matches = re.finditer("mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", sys.stdin.read())

score = 0
enabled = True
for match in matches:
    if (match.group(0) == 'do()'):
        enabled = True
        continue
    if (match.group(0) == 'don\'t()'):
        enabled = False
        continue
    if enabled:
        score += int(match.group(1)) * int(match.group(2))
print(score)

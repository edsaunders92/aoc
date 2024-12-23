import sys

diskmap = [int(i) for i in input()]

disk = list()

is_empty = False
id = 0
for length in diskmap:
    for _ in range(length):
        if (is_empty):
            disk.append('.')
        else:
            disk.append(id)
    if not is_empty:
        id+=1
    is_empty = not is_empty

lp = 0
rp = len(disk) - 1

while lp < rp:
    if disk[lp] != '.':
        lp += 1
        continue
    if disk[rp] == '.':
        rp -= 1
        continue
    temp = disk[lp]
    disk[lp] = disk[rp]
    disk[rp] = temp
    lp += 1
    rp -= 1

score = 0
for i,v in enumerate(disk):
    if v == '.':
        break
    score += i * v
print(score)



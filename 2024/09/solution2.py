import sys

diskmap = [int(i) for i in input()]

disk = list()

is_empty = False
id = 0

for length in diskmap:
    if (is_empty):
        disk.append((length, '.'))
    else:
        disk.append((length, id))
    if not is_empty:
        id+=1
    is_empty = not is_empty

index = len(disk) - 1
while index > 0:
    (length,id) = disk[index]
    if id == '.':
        index -= 1
        continue
    for index2, (length2, id2) in enumerate(disk):
        if id2 != '.':
            continue
        if index2 >= index:
            break
        if length <= length2:
            disk[index] = (length,'.')
            disk[index2] = (length, id)
            disk.insert(1 + index2, (length2 - length, '.'))
            index += 1
            break
    index -= 1


print(disk)

index = 0
score = 0
for length,val in disk:
    for _ in range(length):
        if val != '.':
            score += val * index
        index += 1
print(score)

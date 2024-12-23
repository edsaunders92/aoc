import sys 

def is_report_safe(report):
    pairs = list(set([b - a for a,b in zip(report[:-1], report[1:])]))
    pairs.sort()> 3):
    print(pairs)
    if len(pairs) > 3:
        return False
    if (pairs[0] >= 1 and pairs[-1] <= 3):
        return True
    if (pairs[0] >= -3 and pairs[-1] <= -1):
        return True
    return False

score = 0
for line in map(str.rstrip, sys.stdin):
    a = [int(n) for n in line.split()]
    print(a)
    if (is_report_safe(a)):
        print('hit')
        score += 1
print(score)


    



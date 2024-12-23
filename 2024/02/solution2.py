import sys 

def is_report_safe(report):
    pairs = list(set([b - a for a,b in zip(report[:-1], report[1:])]))
    pairs.sort()
    if len(pairs) > 3:
        return False
    if (pairs[0] >= 1 and pairs[-1] <= 3):
        return True
    if (pairs[0] >= -3 and pairs[-1] <= -1):
        return True
    return False

    print(a)
score = 0
for line in map(str.rstrip, sys.stdin):
    a = [int(n) for n in line.split()]
    for i in range(len(a)):
        if (is_report_safe(a[:i] + a[i+1:])):
            score += 1
            break
print(score)


    



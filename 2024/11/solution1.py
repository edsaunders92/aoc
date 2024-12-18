memo = {}

def count_stones_memo(initial, qty = 25):
    if not (initial, qty) in memo:
        memo[(initial, qty)] = count_stones(initial, qty)
    return memo[(initial, qty)]

def count_stones(initial, qty):
    
    if qty == 0:
        return 1
    qty -= 1

    if initial == 0:
        return count_stones_memo(1, qty)

    n = len(str(initial))
    if n % 2 == 0:
        left = int(str(initial)[:n//2])
        right = int(str(initial)[n//2:])
        return count_stones_memo(left, qty) + count_stones_memo(right, qty)

    return count_stones_memo(initial * 2024, qty)
    

print(sum([count_stones_memo(int(i)) for i in input().split()]))

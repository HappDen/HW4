mon = int(input())
SS = int(input())
for b in range(1, mon // 20 + 1):
    for k in range(( mon - 20 * b ) // 10 + 1):
        t = SS - b - k
        if 20 * b + 10 * k + 5 * t == mon and b >= 1:
            print(b, k, t)
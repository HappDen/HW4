p = int(input())
k = 0
w = 0
for D in range (int(input())):
    A, B = map (int, input().split())
    Ded = A % 25
    fp = A * 50+500+300*A
    w += fp
    s = p * B
    k += s
if k / w > 0.3 :
    print('YES')
else:
    print('NO')
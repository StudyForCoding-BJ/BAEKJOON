#BOJ 1002
import math

for i in range(int(input())):
    xA, yA, rA, xB, yB, rB = map(int, input().split())

    d = math.sqrt(abs(xB-xA)**2 + abs(yB-yA)**2)

    if rA == rB and d == 0:
        print (-1)
    else:
        if rA + rB < d or (rA+rB > d and abs(rA-rB) > d):
            print(0)
        elif rA + rB == d or (rA+rB > d and abs(rA-rB) == d):
            print(1)
        elif rA + rB > d and abs(rA-rB) < d:
            print(2)
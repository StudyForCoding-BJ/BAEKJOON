#BOJ 9375
import sys
tc = int(input())
for i in range(tc):
    n = int(sys.stdin.readline().strip())
    wear = {}
    for j in range(n):
        a, b = map(str, sys.stdin.readline().split())
        if b in wear:
            wear[b].append(a)
        else:
            wear[b] = [a]
    cand = 1
    for key in wear:
        cand *= len(wear[key])+1
    print(cand-1)
#BOJ 10814

import sys

num = int(input())
pplList = [sys.stdin.readline() for i in range(num)]
pplList.sort(key=lambda x: int(x.split()[0]))
print(''.join(pplList))
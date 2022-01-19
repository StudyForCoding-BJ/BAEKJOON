#BOJ 1181

import sys

num = int(input())
strList = list(set([sys.stdin.readline() for i in range(num)]))
strList.sort()
strList.sort(key=lambda x: len(x))
print(''.join(strList))
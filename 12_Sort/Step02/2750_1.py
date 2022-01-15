#BOJ 2750
#129B, 1328ms
import sys

num = int(input())
numlist = [int(sys.stdin.readline()) for i in range(num)]
numlist.sort()
print(*numlist, sep='\n')
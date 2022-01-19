#BOJ 2750
import sys

num = int(input())
numlist = [int(sys.stdin.readline()) for i in range(num)]
numlist.sort()
print(*numlist, sep='\n')
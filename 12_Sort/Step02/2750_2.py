#BOJ 2750
#134B, 1436ms (더 짧게 걸린 다른 코드 보고 적용시켜본건데 오히려 더 길어짐)
import sys

num = int(input())
numlist = [int(sys.stdin.readline()) for i in range(num)]
numlist.sort()
for i in numlist:
    print(i)
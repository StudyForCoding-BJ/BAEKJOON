#BOJ 10250
import math

testcase = int(input())
for i in range(testcase):
    height, width, num = map(int, input().split())
    end = math.ceil(num/height)
    floor = num - height*(end-1)
    print(str(floor) + str(end).zfill(2))
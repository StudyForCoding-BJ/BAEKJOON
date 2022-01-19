#BOJ 1018
import sys

start_w = 0b10101010
start_b = 0b01010101

#input table
n, m = map(int, input().split())
table = []
for i in range(n):
    start = '0b'
    for i in (sys.stdin.readline().strip()):
        if i == 'W':
            start += '1'
        else:
            start += '0'
    
    table.append(start)

#function
def comparison(n, i, diff, startwith, nextwith):
    while n < i+8:
        if n%2==(i%2):
            res = bin(startwith ^ int(table[n][j:j+8], 2))
            diff += res.count('1')
        else:
            res = bin(nextwith ^ int(table[n][j:j+8], 2))
            diff += res.count('1')
        n+=1
    return diff

minimum=[]
for i in range(n-7):
    for j in range(2, m-5):
        n = i
        diff1, diff2 = 0, 0
        diff1 = comparison(n, i, diff1, start_w, start_b)
        diff2 = comparison(n, i, diff2, start_b, start_w)
        minimum.append(diff1)
        minimum.append(diff2)
print(min(minimum))
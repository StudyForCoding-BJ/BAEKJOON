# BOJ 1966
# 80ms
# 30860KB

import sys
input = sys.stdin.readline

N = int(input())

def printer(n, loc, imp):
    count = 0
    front = 0
    rear = 0
    
    while True:
        prior = max(imp)
        
        # ring buffer
        if front == n:
            front = 0 
        if rear == n:
            rear = 0
            
        # pop    
        if imp[front] == prior: 
            if front == loc:
                count+= 1
                print(count)
                return
            imp[front] = 0
            count += 1
            front += 1
            
        # change    
        else: 
            front += 1
            rear += 1
            
for i in range(N):
    n, loc = map(int, input().split())
    imp = list(map(int, input().split()))
    
    printer(n, loc, imp)
num = int(input())

for i in range(num):
    
    H, W, N = map(int, input().split())
    dong = N%H
    ho = N//H + 1
    
    #맨 위층
    if dong == 0:
        dong = H
        ho = ho-1
        
    print(dong *100 + ho)
    

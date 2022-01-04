s = input()

def dial(N):
    if(N == 'A' or N == 'B' or N == 'C'):
        return 3
    elif(N == 'D' or N == 'E' or N == 'F'):
        return 4
    elif(N == 'G' or N == 'H' or N == 'I'):
        return 5
    elif(N == 'J' or N == 'K' or N == 'L'):
        return 6
    elif(N == 'M' or N == 'N' or N == 'O'):
        return 7
    elif(N == 'P' or N == 'Q' or N == 'R' or N == 'S'):
        return 8
    elif(N == 'T' or N == 'U' or N == 'V'):
        return 9
    else:
        return 10

count = 0
for a in s:
    count += dial(a)

print(count)
    
    

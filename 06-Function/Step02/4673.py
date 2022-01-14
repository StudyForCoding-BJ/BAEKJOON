#Elements: int that has constructor (NOT self number)
haveConst = set ()

#create d(n) function.
#haveConst will have only non-self number.
def dn(a: int):
    res = 0
    res = a + (a//10000) + ((a%10000)//1000) + ((a%1000)//100) + ((a%100)//10) + (a%10)
    haveConst.add(res)
    

for i in range (1,10001):
    dn(i)

for i in range (1,10001):
    if i in haveConst:
        continue
    else:
        print (i)
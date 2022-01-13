#BOJ 11729

def mini(a:int) -> list:
    if a == 1:
        return [1,3]
    if a == 2:
        return [1, 2, 1, 3, 2, 3]
    else:
        res = []
        nminus2 = mini(a-2)
        print(nminus2)
        ori_nminus1 = mini(a-1)[-(2**(a-1)):]
        nminus1 = ori_nminus1
        print(nminus1)
        for i in range(len(nminus1)):
            if nminus1[i] == 2:
                nminus1[i] = 3
            elif nminus1[i] == 3:
                nminus1[i] = 2
            else:
                continue
        print(nminus1)
        n = nminus2[-(2**(a-2)):]
        print(n)
        
        from_nminus1 = ori_nminus1[:len(nminus1)-(len(nminus2)-2**(a-2))]
        print(from_nminus1)
        temp1 = from_nminus1[0]
        from_nminus1[0] = from_nminus1[1]
        from_nminus1[1] = temp1
        temp2 = from_nminus1[-1]
        from_nminus1[-1] = from_nminus1[-2]
        from_nminus1[-2] = temp2
        print(from_nminus1)
        
        for i in nminus2:
            res.append(i)
        print(res)
        for i in nminus1:
            res.append(i)
        print(res)
        for i in n:
            res.append(i)
        print(res)
        for i in from_nminus1:
            res.append(i)
        print(res)
        print(nminus2)
        for i in nminus2:
            res.append(i)
        print(res)
        
        return res

num = int(input())
res = mini(num)
print (len(res)//2)
for i in range(len(res)):
    if i == 0 or i%2 == 0:
        print(res[i], end = " ")
    if i%2 != 0:
        print(res[i])
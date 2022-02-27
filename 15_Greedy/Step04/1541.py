#BOJ 1541
a = input()
tmp = ''
nums = []
ops = []

for i in a:
    if i != '+' and i != '-':
        tmp += i
    else:
        ops.append(i)
        nums.append(int(tmp))
        tmp = ''
nums.append(int(tmp))

cal = nums.pop(0)
while nums:
    greedy = 0
    op = ops.pop(0)
    if op == '+':
        cal += nums.pop(0)
    else:
        greedy = nums.pop(0)
        while ops:
            if ops.pop(0) != '-':
                if len(nums) == 0:
                    cal -= greedy
                    break
                else:
                    greedy += nums.pop(0)
            else:
                ops.insert(0, '-')
                break
        cal -= greedy
print(cal)
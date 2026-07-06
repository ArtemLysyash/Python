nums = list(map(int, input().split()))
#p = sum(1 for i in nums if i > 0) генератор
#print(p)
s = 0
for i in nums:
    if i > 0:
        s += 1
print(s)
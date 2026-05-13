def is_armstrong(n):
    sum = 0
    k = 0
    copy = n
    while copy > 0:
        k += 1
        copy //= 10
    copy = n
    while copy > 0:
        c = copy % 10
        sum += c ** k
        copy //= 10
    return sum == n


n = int(input())
p = int(input())
l = 0 # кол во
for i in range(n,p + 1):
    if is_armstrong(i):
        print(i, end = ' ')
        l += 1
if l == 0:
    print(-1)
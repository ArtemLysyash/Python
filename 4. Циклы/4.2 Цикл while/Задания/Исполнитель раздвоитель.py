n = int(input())
l = int(input())
while n > l:
    if n % 2 == 0 and n // 2 > l:
        n = n // 2
        print(f':2')
    else:
        n = n - 1
        print(f'-1')
print(n)
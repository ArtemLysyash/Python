def is_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
count = 0  # кол во простых чисел
b = 2  # число в выводе
while count < n:
    if is_simple(b):
        print(b, end=' ')
        count += 1
    b += 1

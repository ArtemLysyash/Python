def is_perfect(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    return False

n = int(input())
count = 0 # кол во чисел в выводе
b = 2 # число последовательности
while count < n:
    if is_perfect(b):
        print(b ,end = ' ')
        count += 1
    b += 1
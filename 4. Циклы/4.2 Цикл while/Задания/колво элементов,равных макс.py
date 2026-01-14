max = 0
c = 0
while (n := int(input())) != 0:
    if n > max:
        max = n
        c = 1
    elif n == max:
        c += 1
print(c)
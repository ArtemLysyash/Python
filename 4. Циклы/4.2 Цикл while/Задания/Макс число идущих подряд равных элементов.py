max = 0
c = 0
prev = -1
while (n := int(input())) != 0:
    if n == prev:
        c += 1
    else:
        if c > max:
            max = c
        c = 1
    prev = c
    if c > max:
        max = c
print(max)
sum = 0
count = 0
while (number := int(input()))!= 0:
    sum += number
    count += 1
if count > 0:
    a = sum / count
    print(a)
high = list(map(int, input().split()))
x = int(input())
position = 1
for i in range(len(high)):
    if high[i] >= x:
        position += 1
print(position)
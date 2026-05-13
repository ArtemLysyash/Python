def is_palindrome(n):
    original = n
    reversed = 0
    while n > 0:
        reversed = reversed * 10 + n % 10
        n //= 10
    return original == reversed



a = int(input())
b = int(input())
n = 0
for i in range(a,b + 1):
    if is_palindrome(i):
        print(i,end=' ')
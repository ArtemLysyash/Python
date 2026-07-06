nums = list(map(int, input().split()))
a = 0
for i in range(1,len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        a += 1
print(a)
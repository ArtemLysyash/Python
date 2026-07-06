nums = list(map(int,input().split()))
max_index = 0
min_index = 0
for i in range(len(nums)):
    if nums[i] < nums[min_index]:
        min_index = i
    if nums[i] > nums[max_index]:
        max_index = i
nums[min_index],nums[max_index] = nums[max_index],nums[min_index]
print(*nums)
nums = [1,2,3,4,5,3,2,1]
nums.sort()
sum = 0
for i in range(len(nums)):
    if i%2 != 0:
        sum = sum + nums[i]
print(sum)

def findMinValue(nums):
    res = nums[0]
    for num in nums:
        if res < num:
            res = num
    return res





nums = [45,78,12,46,98,66,53,21,63,87,89,91]
result = findMinValue(nums)
print(result)

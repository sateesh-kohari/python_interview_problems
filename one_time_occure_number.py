# get one time occur number
def getOneTimeOccureNumber(nums):
    res =[] 
    for num in nums:
        if num not in res and nums.count(num) == 1:
            res.append(num)    
    return res


nums = [1,2,2,3,3,4,5,5,5,6,6]
result=getOneTimeOccureNumber(nums)
print(result)
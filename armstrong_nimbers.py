def isArmstrongNumber(num):
    nums = str(num)
    n = len(nums)
    total = 0
    for i in nums:
        total += (int(i)**n)

    return True if total == num else False


result = isArmstrongNumber(9)
print(result)
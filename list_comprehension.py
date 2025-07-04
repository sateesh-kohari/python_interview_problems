nums = [3,6,8,12, 14,15]

sqnums = [ num * num if num%2 == 0 else num*num*num for num in nums ]
print(sqnums)
def countVowels(strs):
    vowels = ['a','e','i','o','u']
    count = 0
    for ch in strs:
        if ch in vowels:
            count += 1
    return count

strs = 'this is sateesh'
res = countVowels(strs)
print(res)
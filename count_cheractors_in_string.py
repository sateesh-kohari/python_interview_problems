def countCharInString(strs):
    strs = strs.split(",")
    res = []
    visited = []
    for char in strs:
        if char not in visited:
            visited.append(char)
            res.append(f"{char}:{strs.count(char)}")
    return ",".join(res)


strs = "a,a,a,b,b,c,c,c"
result = countCharInString(strs)
print(result)

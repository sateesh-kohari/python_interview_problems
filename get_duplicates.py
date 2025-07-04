data = ['hello',10,20,40,20,60,40,30]
output = []
for item in data:
    if item not in output and data.count(item) > 1:
        output.append(item)

print(output)
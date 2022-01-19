from unittest import result


arr = [11, 3, 5, 9, 13]
result = []

for i in range(1, max(arr), 2):
    if i not in arr:
        result.append(i)

print(result)

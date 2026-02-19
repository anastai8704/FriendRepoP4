

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
n = len(nums)

for size in [5, 4, 3, 2, 1]:
    row = []
    for _ in range(size):
        row.append(nums[index % n])  
        index += 1
    print(*row)

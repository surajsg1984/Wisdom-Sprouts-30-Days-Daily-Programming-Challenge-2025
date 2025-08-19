def leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')

    # right to left
    for i in range(n-1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    return leaders[::-1]

# Test
arr = [16, 17, 4, 3, 5, 2]
print("Optimized Leaders:", leaders(arr))  # [17, 5, 2]



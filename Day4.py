arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

n = len(arr1)
m = len(arr2)

for i in range(n):
    if arr1[i] > arr2[0]:
        arr1[i], arr2[0] = arr2[0], arr1[i]
        first = arr2[0]
        k = 1
        while k < m and arr2[k] < first:
            arr2[k-1] = arr2[k]
            k += 1
        arr2[k-1] = first
print("arr1:", arr1)
print("arr2:", arr2)

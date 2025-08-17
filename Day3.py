
  ''' one line approch '''
from collections import Counter
findDuplicate_oneliner = lambda arr: next(num for num, freq in Counter(arr).items() if freq > 1)


''' Brute Force (O(n²), O(1)) '''

def findDuplicate_bruteforce(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return arr[i]
''' HashSet (O(n), O(n)) '''

def findDuplicate_set(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

''' Binary Search on Value (O(n log n), O(1)) '''


def findDuplicate_binarySearch(arr):
    low, high = 1, len(arr)-1
    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in arr)
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low

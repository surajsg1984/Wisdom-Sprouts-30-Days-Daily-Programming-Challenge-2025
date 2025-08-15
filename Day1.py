# Sorting Technique by Menu Drival 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr):
    count = [0] * 3
    for num in arr:
        count[num] += 1
    return [0] * count[0] + [1] * count[1] + [2] * count[2]

# Algorithm Call
algorithms = {
    1: {
        "name": "Bubble Sort",
        "func": bubble_sort,
        "time": "O(n²) worst & average, O(n) best",
        "space": "O(1) - in place",
        "approach": "Repeatedly compare adjacent elements and swap if out of order."
    },
    2: {
        "name": "Selection Sort",
        "func": selection_sort,
        "time": "O(n²) for all cases",
        "space": "O(1) - in place",
        "approach": "Find the minimum element and place it in correct position each pass."
    },
    3: {
        "name": "Insertion Sort",
        "func": insertion_sort,
        "time": "O(n²) worst, O(n) best",
        "space": "O(1) - in place",
        "approach": "Insert elements into the sorted portion one by one."
    },
    4: {
        "name": "Merge Sort",
        "func": merge_sort,
        "time": "O(n log n) for all cases",
        "space": "O(n) - extra space",
        "approach": "Divide array into halves, sort each half, then merge."
    },
    5: {
        "name": "Quick Sort",
        "func": quick_sort,
        "time": "O(n log n) avg, O(n²) worst",
        "space": "O(log n) - recursive stack",
        "approach": "Pick pivot, partition array into smaller and greater, sort recursively."
    },
    6: {
        "name": "Counting Sort",
        "func": counting_sort,
        "time": "O(n + k) where k is range",
        "space": "O(n + k)",
        "approach": "Count occurrences of each number, then rebuild array."
    }
}

# Menu display
print("Choose Sorting Technique:")
for key, val in algorithms.items():
    print(f"{key}. {val['name']}")

choice = int(input("Enter choice: "))
if choice in algorithms:
    arr =  [0, 1, 2, 1, 0, 2, 1, 0]
    algo = algorithms[choice]
    sorted_arr = algo["func"](arr.copy())
    print("\n--- Result ---")
    print(f"Sorted Array: {sorted_arr}")
    print(f"Time Complexity: {algo['time']}")
    print(f"Space Complexity: {algo['space']}")
    print(f"Basic Approach: {algo['approach']}")
else:
    print("Invalid choice.")

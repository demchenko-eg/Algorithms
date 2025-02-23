def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def constraint(arr, M):
    s = merge_sort(arr[:])
    ind = {val: i for i, val in enumerate(arr)}
    for i in range(len(s) - 1):
        orig = ind[s[i]]
        next = ind[s[i + 1]]
        if abs(orig - next) > 1 and s[i] + s[i + 1] > M:
            return "No"
    return "Yes"

n, M = map(int, input().split())
masses = list(map(int, input().split()))
print(constraint(masses, M))
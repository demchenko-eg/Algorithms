def f(arr, t):
    n = len(arr)
    if n <= 1:
        return arr, 0
    mid = n // 2
    left, cnt_left = f(arr[:mid], t)
    right, cnt_right = f(arr[mid:], t)
    count = cnt_left + cnt_right
    j = 0
    for x in left:
        while j < len(right) and right[j] < x - t:
            j += 1
        count += j
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, count

n, t = map(int, input().split())
arr = list(map(int, input().split()))
_, result = f(arr, t)
print(result)
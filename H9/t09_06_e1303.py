def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    result = []
    i = j = inv_count = 0
    inv_count += left_inv + right_inv
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count


while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    _, swaps = merge_sort(arr)
    print(swaps)

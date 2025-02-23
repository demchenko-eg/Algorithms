def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
sorted_arr = merge_sort(arr)
for robot in sorted_arr:
    print(robot[0], robot[1])
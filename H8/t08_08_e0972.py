def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
sorted_times = quick_sort(times)
for time in sorted_times:
    print(*time)
def bubble_sort(arr):
    n = len(arr)
    c = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                c += 1
    return c

n = int(input())
lst = list(map(int, input().split()))
print(bubble_sort(lst))
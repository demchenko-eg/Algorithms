def insertion_sort(arr):
    n = len(arr)
    sn = True
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if j != i - 1:
            sn = False
            print(" ".join(map(str, arr)))
    if sn:
        return

n = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr)
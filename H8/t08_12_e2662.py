def selection_moves(arr):
    n = len(arr)
    first_elem = arr[0]
    moves = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            if arr[min_index] == first_elem:
                moves += 1
            elif arr[i] == first_elem:
                moves += 1
    return moves

n = int(input())
arr = list(map(int, input().split()))
print(selection_moves(arr))
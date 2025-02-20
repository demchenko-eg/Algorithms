def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def selection_sort(l):
    n = len(l)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and key < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left_half = l[:mid]
        right_half = l[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1
    return l

def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# l = [64, 34, 25, 12, 22, 11, 90]
# print("Bubble Sort:", bubble_sort(l[:]))
# print("Selection Sort:", selection_sort(l[:]))
# print("Insertion Sort:", insertion_sort(l[:]))
# print("Merge Sort:", merge_sort(l[:]))
# print("Quick Sort:", quick_sort(l[:]))
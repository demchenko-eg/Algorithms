def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        sorted_arr = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            left_key = (left_half[i] % 10, left_half[i])
            right_key = (right_half[j] % 10, right_half[j])
            if left_key < right_key:
                sorted_arr.append(left_half[i])
                i += 1
            else:
                sorted_arr.append(right_half[j])
                j += 1
        sorted_arr.extend(left_half[i:])
        sorted_arr.extend(right_half[j:])
        return sorted_arr
    return arr

n = int(input().strip())
numbers = [int(input().strip()) for _ in range(n)]
sorted_numbers = merge_sort(numbers)
print(" ".join(map(str, sorted_numbers)))
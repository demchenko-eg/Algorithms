def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def f2(current, lst, u):
    if len(current) == len(lst):
        print("".join(current))
        return
    for i in range(len(lst)):
        if u[i]:
            continue
        if i > 0 and lst[i] == lst[i - 1] and not u[i - 1]:
            continue
        u[i] = True
        current.append(lst[i])
        f2(current, lst, u)
        current.pop()
        u[i] = False

s = input().strip()
s_list = list(s)
sorted_s = insertion_sort(s_list)
u = [False] * len(sorted_s)
f2([], sorted_s, u)
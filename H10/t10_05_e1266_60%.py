def f1(index, curr, tracks, leng):
    if index == len(tracks):
        return curr
    best = f1(index + 1, curr, tracks, leng)
    if curr + tracks[index] <= leng:
        best = max(best, f1(index + 1, curr + tracks[index], tracks, leng))
    return best

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    data = list(map(int, line.split()))
    lenght = data[0]
    count = data[1]
    tracks = data[2:]
    result = f1(0, 0, tracks, lenght)
    print("sum:" + str(result))





# def f2(index, curr, best, tracks, maxl, s1):
#     if curr == maxl:
#         return maxl
#     if index == len(tracks):
#         return max(curr, best)
#     if curr + s1[index] <= best:
#         return best
#     result_exclude = f2(index + 1, curr, best, tracks, maxl, s1)
#     best = max(best, result_exclude)
#     if curr + tracks[index] <= maxl:
#         result_include = f2(index + 1, curr + tracks[index], best, tracks, maxl, s1)
#         best = max(best, result_include)
#     return best

# while True:
#     try:
#         line = input().strip()
#     except EOFError:
#         break
#     if not line:
#         continue
#     data = list(map(int, line.split()))
#     maxl = data[0]
#     tracks = data[2:]
#     n = len(tracks)
#     s1 = [0] * (n + 1)
#     for i in range(n - 1, -1, -1):
#         s1[i] = s1[i + 1] + tracks[i]
#     result = f2(0, 0, 0, tracks, maxl, s1)
#     print("sum:" + str(result))





# def f3(n, tracks, index=0, curr=0):
#     if index == len(tracks) or curr == n:
#         return curr
#     if curr + tracks[index] <= n:
#         include = f3(n, tracks, index + 1, curr + tracks[index])
#     else:
#         include = 0
#     exclude = f3(n, tracks, index + 1, curr)
#     return max(include, exclude)

# while True:
#     try:
#         line = input().strip()
#         if not line:
#             break
#         data = list(map(int, line.split()))
#         n, tracks = data[0], data[2:]
#         print(f"sum:{f3(n, tracks)}")
#     except EOFError:
#         break
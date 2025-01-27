def animals():
    n = int(input())
    if n > 0:
        colors = list(map(int, input().split()))
    else:
        colors = []
        input()    ###
    m = int(input())
    queries = list(map(int, input().split()))
    def lower_bound(array, value):
        left, right = 0, len(array)
        while left < right:
            mid = (left + right) // 2
            if array[mid] < value:
                left = mid + 1
            else:
                right = mid
        return left
    def upper_bound(array, value):
        left, right = 0, len(array)
        while left < right:
            mid = (left + right) // 2
            if array[mid] <= value:
                left = mid + 1
            else:
                right = mid
        return left
    results = []
    for query in queries:
        lb = lower_bound(colors, query)
        ub = upper_bound(colors, query)
        results.append(ub - lb)
    print("\n".join(map(str, results)))

animals()

def can_place_cows(intervals, n, d):
    count = 0
    last_pos = None
    for a, b in intervals:
        pos = a if last_pos is None else max(a, last_pos + d)
        while pos <= b:
            count += 1
            if count == n:
                return True
            last_pos = pos
            pos += d
    return False

def max_min_distance(n, intervals):
    left, right = 1, intervals[-1][1] - intervals[0][0] 
    ans = 1 
    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(intervals, n, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


n, m = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(m)]
intervals.sort()
print(max_min_distance(n, intervals))

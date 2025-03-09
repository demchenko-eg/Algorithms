def f9(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
            a = nums[i]
            b = nums[j]
            results = [a + b, a - b, b - a, a * b]
            if abs(b) > 1e-6:
                results.append(a / b)
            if abs(a) > 1e-6:
                results.append(b / a)
            for res in results:
                if f9(next_nums + [res]):
                    return True
    return False

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    print("YES" if f9([a, b, c, d]) else "NO")
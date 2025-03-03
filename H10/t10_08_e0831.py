def f(i, total, expr, n, s, numbers):
    if i == n:
        if total == s:
            return expr + "=" + str(s)
        return None
    res = f(i + 1, total + numbers[i], expr + "+" + str(numbers[i]), n, s, numbers)
    if res:
        return res
    res = f(i + 1, total - numbers[i], expr + "-" + str(numbers[i]), n, s, numbers)
    return res

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
result = f(1, numbers[0], str(numbers[0]), n, s, numbers)
print(result if result else "No solution")
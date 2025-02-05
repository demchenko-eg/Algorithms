def find_x(C):
    left, right = 0, max(1, C)
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if mid**2 + mid**0.5 < C:
            left = mid
        else:
            right = mid
    return round(left, 6)

C = float(input())
print(f"{find_x(C):.6f}")